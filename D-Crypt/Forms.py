"""
Name: Ko Jia Ling
Admin No.: 190681D
Module Group: IT2554-03

Practical Assignment 1
D-Crypt
Forms.py
"""

from wtforms import Form, SelectField, TextAreaField, RadioField, IntegerField, StringField, validators

class ShiftCipherForm(Form):
    numberList = list(range(1,26+1))

    encryptionString = RadioField('', choices=[('alpha', 'Encrypt/Decrypt only Uppercase and Lowercase characters'),
                                               ('base64', 'Encrypt/Decrypt all Base64 characters')]
                                  , default='alpha')

    shiftKey = SelectField('Key:', choices=numberList, default='3')

    inputText = TextAreaField('Input'
                              , validators=[validators.DataRequired(message='This is a required field.')]
                              , render_kw={"rows": 5})

    outputText = TextAreaField('Output', render_kw={"rows": 5})


class RailFenceForm(Form):
    railKey = IntegerField('Key: ', [validators.NumberRange(min=1, max = 100, message="This application only supports rail key value of 1 to 100.")])

    encryptionString = RadioField('', choices=[('space', 'Encrypt/Decrypt with Spaces'),
                                               ('no-space', 'Remove all Spaces')]
                                  , default='space')

    inputText = TextAreaField('Input'
                              , validators=[validators.DataRequired(message='This is a required field.')]
                              , render_kw={"rows": 5})

    outputText = TextAreaField('Output', render_kw={"rows": 5})


class AesForm(Form):
    mode = SelectField('Mode:', choices=['ECB', 'CBC', 'CFB', 'OFB'], default='ECB')

    keySize = SelectField('Key Size (bits):', choices=['128', '192', '256'], default='128')

    key = StringField('Key: ', [validators.DataRequired()])

    iv = StringField('IV: ')

    inputText = TextAreaField('Input'
                              , validators=[validators.DataRequired(message='This is a required field.')]
                              , render_kw={"rows": 5})

    outputText = TextAreaField('Output', render_kw={"rows": 5})


class ColumnarTranspositionForm(Form):
    key = StringField('Key: ', [validators.DataRequired()])

    encryptionString = RadioField('', choices=[('space', 'Encrypt/Decrypt with Spaces'),
                                               ('no-space', 'Remove all Spaces')]
                                  , default='space')

    inputText = TextAreaField('Input'
                              , validators=[validators.DataRequired(message='This is a required field.')]
                              , render_kw={"rows": 5})

    outputText = TextAreaField('Output', render_kw={"rows": 5})


class VernamCipherForm(Form):
    key = StringField('Pad: ', [validators.DataRequired()])

    inputText = TextAreaField('Input'
                              , validators=[validators.DataRequired(message='This is a required field.')]
                              , render_kw={"rows": 5})

    outputText = TextAreaField('Output', render_kw={"rows": 5})

class MonoalphabetCipherForm(Form):
    key = StringField('Key: ', [validators.DataRequired()])

    inputText = TextAreaField('Input'
                              , validators=[validators.DataRequired(message='This is a required field.')]
                              , render_kw={"rows": 5})

    outputText = TextAreaField('Output', render_kw={"rows": 5})

class DiffieHellmanKeyExchangeForm(Form):
    primeOne = IntegerField('n (prime number): ', [validators.DataRequired()])
    primeTwo = IntegerField('g (prime number): ', [validators.DataRequired()])
    privateOne = IntegerField('A (random integer): ', [validators.DataRequired()])
    privateTwo = IntegerField('B (random integer): ', [validators.DataRequired()])
    keyOne = IntegerField('K1 (secret key): ', [validators.DataRequired()])
    keyTwo = IntegerField('K2 (secret key): ', [validators.DataRequired()])