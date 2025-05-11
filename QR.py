import qrcode

## taking UPI id as a input 
upi_id=input("Enter your upi id :- ")

## upi://pay?pa=UPI_ID&pa=NAME&am=AMOUNT&cu=CURRANCY&tn=MESSGE

## defining the payment URL based on the upi and payment app
## even you can modify there URL based on the payment app which you want to support

phonepe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
googlepay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
navi_url=f'upi://pay?pa={upi_id}&pa=Recipient%20Name&mc=1234'   ## mc:- mearchant code, it is optional


### create QR code for each payment app

phonepe_qr=qrcode.make(phonepe_url)
googlepay_qr=qrcode.make(googlepay_url)
paytm_qr=qrcode.make(paytm_url)
navi_qr=qrcode.make(navi_url)

## save the qr code to image file (optonal)

phonepe_qr.save('phonepe_qr.png')
googlepay_qr.save('googlepay_qr.png')
paytm_qr.save('paytm_qr.png')
navi_qr.save('navi_qr.png')

 

## Dispaley the QR code (you may need to isntall pil/pillow library)

phonepe_qr.show()
googlepay_qr.show()
paytm_qr.show()
navi_qr.show()



