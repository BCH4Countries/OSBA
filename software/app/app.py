from webbrowser import get
from bitcash import PrivateKey, Key
from bitcash.format import hex_to_wif
from bitcash.network import currency_to_satoshi_cached, satoshi_to_currency_cached
from dotenv import load_dotenv
from appJar import gui
from appJar.appjar import WIDGET_NAMES
import datetime
import requests
import serial
import random
import string
import qrcode
import json
import time
import os


if os.environ.get('DISPLAY', '') == '':
    os.environ.__setitem__('DISPLAY', ':0.0')


def log(msg):
    if (msg == ''): return
    day = f"{datetime.datetime.now():%d}"
    month = f"{datetime.datetime.now():%m}"
    logDir = f'./logs/{month}/'
    logFile = f'./logs/{month}/{day}.txt'
    if not (os.path.isdir(logDir)):
        os.mkdir(logDir)
    logFileObject = open(logFile, 'a')
    logLine = f'[{datetime.datetime.now():%Y-%m-%d %I:%M:%S}] {msg} \n';
    logFileObject.write(logLine)
    logFileObject.close()
    print(logLine)


load_dotenv()
log('Starting...')
time.sleep(10)
log('Started')
premiumRate = float(os.environ.get('PREMIUM', '0.02'))
credit = 0
credit_ = 0
apex = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=1)

# Output Varibles
outputBCH = ""
outputName = ""
outputKey = False
outputKeyAddress = ""
outputTXString = ""
shouldPrint = False
shouldCreateTX = False
shouldCreateWallet = False

# BCH Prices
bch = False
bchBuyPrice = False
while not (bch and bchBuyPrice):
    try:
        log(f'Updating BCH price')
        bchValue = currency_to_satoshi_cached(1, 'usd')
        bchBuyPrice = satoshi_to_currency_cached(100000000, 'usd')
        log(f'$1 USD = ₿ {bchValue}')
        log(f'₿ 1 = $USD {str(bchBuyPrice)}')
    except:
        print("An exception occurred while getting BCH Prices")
        time.sleep(5)

# Init ATM wallet
log(f'Loading ATM wallet')
mainWallet = Key(os.environ.get('MAIN_PRIVATE_KEY'))
balance = str(mainWallet.get_balance('bch'))
log(f'ATM wallet balance: ₿{balance}')

app = gui("ATM", os.environ.get('DISPLAY_SIZE', 'fullscreen'))

def serialLoop(): 
    global shouldPrint
    global shouldCreateTX
    global shouldCreateWallet
    global credit
    global bch

    # AB: Very poor code, imporve. I should have used electron.
    if (shouldPrint):
        shouldPrint = False
        printWallet()
    elif (shouldCreateTX):
        shouldCreateTX = False
        createTX()
    elif (shouldCreateWallet):
        shouldCreateWallet = False
        createWallet()
    else:
        input = apex.readline().decode("utf-8").rstrip().lstrip()
        log(input)
        
        if (input == '$1 Credit'):
            credit = credit + 1
            print(credit)
        if (input == '$5 Credit'):
            credit = credit + 5
            print(credit)
        if (input == '$10 Credit'):
            credit = credit + 10
            print(credit)
        if (input == '$20 Credit'):
            credit = credit + 20
            print(credit)
        if (input == '$50 Credit'):
            credit = credit + 50
            print(credit)
        if (input == '$100 Credit'):
            credit = credit + 100
            print(credit)
        
        if (credit > 0):
            app.setFont(size=70)
            app.setLabel('line3', 'Premium: ' + str(premiumRate*100) + '%')
            app.setLabel('line1', '$'+str(credit))
            credit_ = creditSubtractPremium()
            bch_ = bch*credit_
            app.setLabel('line2', f'≈ ₿{bch_:.8f}')
            
        if (input == 'PRINT'):
            app.hideWidgetType(WIDGET_NAMES.Label, 'line1')
            app.hideWidgetType(WIDGET_NAMES.Label, 'line3')
            app.setLabel('line2', f'Creating Wallet...')
            shouldCreateWallet = True


def createWallet():
    global shouldCreateTX
    global outputKey
    global outputKeyAddress
    global outputName
    log(f'createWallet()')

    outputKey = Key()
    outputKeyAddress = outputKey.address
    outputName = ''.join(random.choices(string.ascii_lowercase, k=10))
    app.setLabel('line2', f'Signing Transaction...')
    shouldCreateTX = True

def createTX():
    global shouldPrint
    global outputTXString
    global outputKeyAddress
    global outputBCH
    global credit
    log(f'createTX()')

    # Calculate outputBCH
    credit_ = creditSubtractPremium()
    log(f'credit: {credit}')
    log(f'creditSubtractPremium: {credit_}')
    bchCreditValueRequest = currency_to_satoshi_cached(credit_, 'usd')
    outputBCH = bchCreditValueRequest.text
    log(f'profit: {credit - credit_}')
    log(f'creditSubtractPremium as BCH: {outputBCH}')

    # Make Transaction
    outputTXString = mainWallet.create_transaction([(outputKeyAddress, outputBCH, 'bch')])
    app.setLabel('line2', f'Printing Recipt...')
    shouldPrint = True
    
def printWallet():
    global bchBuyPrice
    global credit
    global outputName
    global outputKey
    global outputBCH
    global outputKeyAddress
    global outputTXString
    global outputShouldPrint
    global outputShouldCreateTX
    global outputShouldCreateWallet
    log(f'printWallet()')

    os.system(f'mkdir -p ./output/{outputName}')
    os.system(f'cp ./wallet/index.html ./output/{outputName}')
    os.system(f'cp ./wallet/background.jpeg ./output/{outputName}')
    os.system(f'cp ./wallet/ticketing.ttf ./output/{outputName}')

    privateKey = hex_to_wif(outputKey.to_hex(), compressed=False)

    publicKeyQR = qrcode.make(outputKeyAddress)
    publicKeyQR.save(f'./output/{outputName}/public.png')
    statusQR = qrcode.make(f'https://www.blockchain.com/bch/tx/{outputTXString}') # TODO: replace URL
    statusQR.save(f'./output/{outputName}/status.png')
    privateKeyQR = qrcode.make(privateKey)
    privateKeyQR.save(f'./output/{outputName}/private.png')

    with open(f'./output/{outputName}/index.html', 'r') as file:
        data = file.read()
        data = data.replace('[BCH]', f'₿{float(outputBCH):.8f}')
        data = data.replace('[CURRENCY]', 'BITCOIN')
        data = data.replace('[TIME]', f"{datetime.datetime.now():%I:%M:%S}")
        data = data.replace('[DATE]', f"{datetime.datetime.now():%Y-%m-%d}")
        data = data.replace('[ADDRESS]', outputKeyAddress)
        data = data.replace('[TX]', outputTXString)
        data = data.replace('[PRIVATE_KEY]', privateKey)
    with open(f'./output/{outputName}/index.html', 'w') as file:
        file.write(data)

    os.system(f'wkhtmltopdf -q --page-height 150 --page-width 100 -O Landscape ./output/{outputName}/index.html ./output/{outputName}/wallet.pdf')
    os.system(f'lp -h localhost:631 ./output/{outputName}/wallet.pdf')
    time.sleep(1)
    apex.flush()
    credit = 0;
    apex.write(b"RESET\n")
    apex.flush()
    time.sleep(1)
    os.system(f'rm -rf ./output/{outputName}')
    
    # Reset UI
    updateBCHBuyPrice = satoshi_to_currency_cached(100000000, 'usd')
    bchBuyPrice = updateBCHBuyPrice
    app.setFont(size=50)
    app.showWidgetType(WIDGET_NAMES.Label, 'line1')
    app.showWidgetType(WIDGET_NAMES.Label, 'line3')
    app.setLabel('line1', 'Open-Source Bitcoin ATM')
    app.setLabel('line2', 'Insert Cash To Begin')
    app.setLabel('line3', '1 BCH = $' + str(bchBuyPrice))

    # Update balance
    balance = str(mainWallet.get_balance('bch'))
    log(f'ATM wallet balance: ₿{balance}')

    # Reset output varibales
    outputBCH = ""
    outputName = ""
    outputKey = False
    outputKeyAddress = ""
    outputTXString = ""
    outputShouldPrint = False
    outputShouldCreateTX = False
    outputShouldCreateWallet = False

def creditSubtractPremium():
    global credit
    credit_ = credit - (credit * premiumRate)
    return credit_

app.setFont(size=50)
app.setBg("#292D39")
app.setFg("white")
app.registerEvent(serialLoop)
app.setStretch('both')
app.setSticky('news')
app.addLabel('line1', 'Open-Source Bitcoin Cash (BCH) ATM')
app.addLabel('line2', 'Insert Cash To Begin')
app.addLabel('line3', '1 BCH = $' + str(bchBuyPrice))
app.go()
