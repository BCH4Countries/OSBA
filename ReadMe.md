# OSCA - Open-Source Bitcoin Cash ATM

The Open-Source Bitcoin Cash ATM, a Bitcoin Cash ATM that someone with minimal electro-mechanical skill can build at home with parts from Amazon and hardware from Lowes. OSBA does not require you to disclose any personal information to use this ATM. The user inserts cash and the machine returns a cold wallet loaded with the desired amount of Bitcoin Cash.

  
*This project is still in beta and is in active development.*
  

<p align="center">
    <img width="350"  src="https://github.com/jettscythe/OSBCHATM/blob/master/misc/osca.jpg?raw=true"  alt="OSCA">
</p>

  
  

### Instructions
Detailed step-by-step instructions and a video tutorial are coming soon. However you can find all of the software and plans in this repo.
- [Build Instructions](https://github.com/jettscythe/OSBCHATM/blob/master/instructions/Instructions.md)


### Usecases

- Accept Bitcoin Cash - Want to accept Bitcoin Cash at your business? Use OSBA to provide your customers a easy way to purchase Bitcoin Cash without a middle man.

- Passive Income - Use the commission feature to earn a commission on each transaction.
  
- Fungibility - Make Bitcoin Cash more fungibile by allowing anyone to anonymously convert hard fiat currency into Bitcoin Cash.

  

### How does it work?

OSBA is very simple to use. Simply insert the amount of cash you would like converted to Bitcoin then press the blue flashing button. 

<p align="center">
    <img  width="400"  src="https://github.com/jettscythe/OSBCHATM/blob/master/misc/demo.gif?raw=true" alt="Demo">
</p>

A paper wallet will be printed that is loaded with the desired amount of Bitcoin. Scan the status QR code to see your transaction on blockchain. Scan the withdraw QR code on the right to sweep the paper wallet. 

<p align="center">
    <img  width="400"  src="https://github.com/jettscythe/OSBCHATM/blob/master/misc/wallet.gif?raw=true" alt="Demo">
</p>
  

### Motivation

The orginially Github was discovered on r/bitcoin by u/SoiledCold5 the day it was released. The orginially github and it's creator made it solely for Bitcoin but as days went by, it was left dormant with little to no adoption by users. The problem was that Bitcoin Core is not built to be a currency due to it's high fees and long wait times. Eventually u/SoiledCold5 made a request on the Bitcoin Cash telegram to fork the orginial Git to make it for Bitcoin Cash.

Bitcoin Cash has power to revolutionise finance. However anonymously converting fiat currency into crypto is becoming harder and harder. All of the major crypto exchanges require disclosure of personal identifiable information. Even the Bitcoin ATMs at your local gas station require a cell phone number and an email address. Crypto-currencies are so much of a threat to the legacy banking system that the UK has banned Bitcoin ATMs outright. This concerns me because I believe if we remain on this course open-source technology like blockchain will become heavily regulated and corporatized.

  

The Open-Source Bitcoin Cash ATM aims to remedy these issues by making it safe, easy and anonymous for anyone to convert hard fiat currency into digital cryptocurrency. The machine has been deliberately designed so someone with minimal electro-mechanical skill can build this ATM at home with a few off the shelf electronics and trip to the local hardware store.

  

By making this project open-source I hope others will contribute to this project and extend the software to work with other popular crypto-currencies. Over the long-term I hope that anonymous crypto ATMs will make crypto more accessible and fungible.

  
  

### FAQ

#### How can I trust this machine?

**YOU CAN’T**. I’ll say that again, you can’t trust this machine if you see it in the wild. A malicious actor could simply not load the paper wallet or save a copy of each private key it generates. So why build it then? My vision is that in the short to medium-term these kind of machines will be operated by independent businesses (gas stations, gun stores, smoke shops, etc) and the customers will trust the operator, not the machine per se. A user can easily test if the wallet is being loaded or not with a $5 transaction. Always remember to withdraw the value of the paper wallet to a secure wallet as soon as possible.

  

#### Why use paper wallets?

Paper wallets are controversial because they are considered outdated and unsecure, however I believe this is a perfect use case. While admittedly they have their drawbacks, paper wallets allow for the most anonymous method of exchanging cash for cryptocurrency. Any digital method could potentially expose the identity of the recipient. Furthermore any digital method of exchange would require the user to have a smartphone to use this machine, which not everybody has. I see no reason why cryptocurrencies must exist exclusively in the digital domain.

  

#### Why use concrete not metal?

Consider the Venn diagram of the parameters of this project. A) It must be easy to build B) Require minimal skill to build C) Must be cheap and extremely robust. While metal has obvious advantages (not least of which aesthetic), it requires skill to work with and expensive tools. Concrete is very cheap, it’s easy to work with and is exceptionally strong. Therefore concrete is the obvious choice.

  

#### Why ~~Bitcoin~~ Bitcoin Cash? 

https://whybitcoincash.com/
