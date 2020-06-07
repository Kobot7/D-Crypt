"""
Name: Ko Jia Ling
Admin No.: 190681D
Module Group: IT2554-03

Practical Assignment 1
D-Crypt
main.py
"""

from flask import Flask, render_template, request, redirect
import Forms
import cipher

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def default():
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('home.html', currentPage="home")




@app.route('/cipher/aes')
def aes():
    error = False
    aesForm = Forms.AesForm(request.form)

    mode = request.args.get('mode', default='ECB')
    keySize = request.args.get('keySize', default='128')
    key = request.args.get('key', default='u8qDRkSP2P=JB1jl')
    iv = request.args.get('iv', default='Vo2rek-P2Pw0l4jd')
    inputText = request.args.get('inputText', default='Hello World!')
    action = request.args.get('submit', default='Encrypt')

    try:
        if action == 'Encrypt':
            if mode == 'ECB':
                outputText = cipher.AES.encrypt_ECB(inputText, key)
            elif mode == 'CBC':
                outputText = cipher.AES.encrypt_CBC(inputText, key, iv)
            elif mode == 'CFB':
                outputText = cipher.AES.encrypt_CFB(inputText, key, iv)
            else:
                outputText = cipher.AES.encrypt_OFB(inputText, key, iv)

        else:
            if mode == 'ECB':
                outputText = cipher.AES.decrypt_ECB(inputText, key)
            elif mode == 'CBC':
                outputText = cipher.AES.decrypt_CBC(inputText, key, iv)
            elif mode == 'CFB':
                outputText = cipher.AES.decrypt_CFB(inputText, key, iv)
            else:
                outputText = cipher.AES.decrypt_OFB(inputText, key, iv)

    except:
        error = True

    else:
        aesForm.outputText.data = outputText

    aesForm.mode.data = mode
    aesForm.keySize.data = keySize
    aesForm.key.data = str(key)
    aesForm.iv.data = str(iv)
    aesForm.inputText.data = inputText

    return render_template('aes.html', currentPage="aes", cipherForm = aesForm, error=error)

@app.route('/cipher/mono-alphabet-cipher')
def monoalphabetCipher():
    error = False
    monoalphabetCipherForm = Forms.MonoalphabetCipherForm(request.form)

    key = request.args.get('key', default='AZERTYUIOPQSDFGHJKLMWXCVBN')
    inputText = request.args.get('inputText', default='Hello World!')
    action = request.args.get('submit', default='Encrypt')

    try:
        if action == 'Encrypt':
            outputText = cipher.Monoalphabet_Cipher.encrypt(inputText, key)

        else:
            outputText = cipher.Monoalphabet_Cipher.decrypt(inputText, key)

    except:
        error = True

    else:
        monoalphabetCipherForm.outputText.data = outputText

    monoalphabetCipherForm.key.data = key
    monoalphabetCipherForm.inputText.data = inputText

    return render_template('mono-alphabet-cipher.html', currentPage="mono-alphabet-cipher", cipherForm=monoalphabetCipherForm, error=error)

@app.route('/cipher/rail-fence-technique')
def railFenceTechnique():
    error = False
    railFenceForm = Forms.RailFenceForm(request.form)

    railKey = request.args.get('railKey', default='3')
    encryptionString = request.args.get('encryptionString', default='space')
    inputText = request.args.get('inputText', default='Hello World!')
    action = request.args.get('submit', default='Encrypt')

    try:
        if action == 'Encrypt':
            outputText = cipher.Rail_Fence_Technique.encrypt(inputText, int(railKey), encryptionString)

        else:
            outputText = cipher.Rail_Fence_Technique.decrypt(inputText, int(railKey), encryptionString)

    except:
        error = True

    else:
        railFenceForm.outputText.data = outputText

    railFenceForm.railKey.data = str(railKey)
    railFenceForm.encryptionString.data = encryptionString
    railFenceForm.inputText.data = inputText

    return render_template('rail-fence-technique.html', currentPage="rail-fence-technique", cipherForm = railFenceForm, error=error)

@app.route('/cipher/shift-cipher')
def shiftCipher():
    error = False
    shiftCipherForm = Forms.ShiftCipherForm(request.form)

    shiftKey = request.args.get('shiftKey', default='3')
    encryptionString = request.args.get('encryptionString', default='alpha')
    inputText = request.args.get('inputText', default='Hello World!')
    action = request.args.get('submit', default='Encrypt')

    try:
        if action=='Encrypt':
            outputText = cipher.Shift_Cipher.encrypt(int(shiftKey), inputText, encryptionString)

        else:
            outputText = cipher.Shift_Cipher.decrypt(int(shiftKey), inputText, encryptionString)

    except:
        error = True

    else:
        shiftCipherForm.outputText.data = outputText

    shiftCipherForm.shiftKey.data = str(shiftKey)
    shiftCipherForm.encryptionString.data = encryptionString
    shiftCipherForm.inputText.data = inputText

    return render_template('shift-cipher.html', currentPage="shift-cipher", cipherForm = shiftCipherForm, error=error)

@app.route('/cipher/simple-columnar-transposition-technique')
def columnarTranspositionTechnique():
    error = False
    columnarTransposition = Forms.ColumnarTranspositionForm(request.form)

    key = request.args.get('key', default='CRYPT')
    encryptionString = request.args.get('encryptionString', default='space')
    inputText = request.args.get('inputText', default='Hello World!')
    action = request.args.get('submit', default='Encrypt')

    try:
        if action == 'Encrypt':
            outputText = cipher.Simple_Columnar_Transposition_Technique.encrypt(inputText, key, encryptionString)

        else:
            outputText = cipher.Simple_Columnar_Transposition_Technique.decrypt(inputText, key, encryptionString)

    except:
        error = True

    else:
        columnarTransposition.outputText.data = outputText

    columnarTransposition.key.data = str(key)
    columnarTransposition.encryptionString.data = encryptionString
    columnarTransposition.inputText.data = inputText

    return render_template('simple-columnar-transposition-technique.html', currentPage="simple-columnar-transposition-technique", cipherForm = columnarTransposition, error=error)

@app.route('/cipher/vernam-cipher')
def vernamCipher():
    error = False
    vernamCipherForm = Forms.VernamCipherForm(request.form)
    key = request.args.get('key', default='JEISKFOXMD')
    inputText = request.args.get('inputText', default='HELLOWORLD')
    action = request.args.get('submit', default='Encrypt')

    try:
        if action == 'Encrypt':
            outputText = cipher.Vernam_Cipher.encrypt(inputText, key)

        else:
            outputText = cipher.Vernam_Cipher.decrypt(inputText, key)

    except:
        error = True

    else:
        vernamCipherForm.outputText.data = outputText

    vernamCipherForm.key.data = key
    vernamCipherForm.inputText.data = inputText

    return render_template('vernam-cipher.html', currentPage="vernam-cipher", cipherForm = vernamCipherForm, error=error)

@app.route('/cipher/diffie-hellman-key-exchange')
def deffieHellmanKeyExchange():
    error = False
    diffieHelllman = Forms.DiffieHellmanKeyExchangeForm(request.form)

    n = request.args.get('primeOne', default='23')
    g = request.args.get('primeTwo', default='59')
    A = request.args.get('privateOne', default='82')
    B = request.args.get('privateTwo', default='70')

    try:
        secretKey = cipher.Diffie_Hellman_Key_Exchange.calculate(n, g, A, B)

    except:
        error = True

    else:
        diffieHelllman.keyOne.data = secretKey
        diffieHelllman.keyTwo.data = secretKey

    diffieHelllman.primeOne.data = n
    diffieHelllman.primeTwo.data = g
    diffieHelllman.privateOne.data = A
    diffieHelllman.privateTwo.data = B

    return render_template('diffie-hellman-key-exchange.html', currentPage='diffie-hellman-key-exchange', form=diffieHelllman, error=error)



@app.route('/learn/types-of-attack')
def learnTypesOfAttack():
    return render_template('learn-types-of-attack.html', currentPage='learn-types-of-attack')

@app.route('/learn/shift-cipher')
def learnShiftCipher():
    return render_template('learn-shift-cipher.html', currentPage='learn-shift-cipher')

@app.route('/learn/vernam-cipher')
def learnVernamCipher():
    return render_template('learn-vernam-cipher.html', currentPage='learn-vernam-cipher')

@app.route('/learn/rail-fence-technique')
def learnRailFenceTechnique():
    return render_template('learn-rail-fence-technique.html', currentPage='learn-rail-fence-technique')

@app.route('/learn/mono-alphabet-cipher')
def learnMonoalphabetCipher():
    return render_template('learn-mono-alphabet-cipher.html', currentPage='learn-mono-alphabet-cipher')

@app.route('/learn/simple-columnar-transposition-technique')
def learnSimpleColumnarTransposition():
    return render_template('learn-simple-columnar-transposition.html', currentPage='learn-simple-columnar-transposition-technique')



if __name__=='__main__':
    app.run(debug=True)