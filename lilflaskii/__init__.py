#lilflaskii.py

import os
from flask import Flask, render_template, request
import stripe

tbool=True

#establish stripe plan names here
plans = {
	'plan1',
	'plan2',
	'plan80',
}

#grab api keys
stripe_keys = {
	'secret_key': os.environ['STRIPE_PRIVATE'],
	'publishable_key' : os.environ['STRIPE_PUBLIC'],
}

if tbool is True:
	stripe.api_key = stripe_keys['tsecret_key']
else:
	stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)

@app.route('/subscribe1', methods=['POST'])
def charge():

	customer = stripe.Customer.create(
		email=request.form['stripeEmail'],
		source=request.form['stripeToken'],
	)


	sub = stripe.Subscription.create(
		customer=customer.id,
		plan='plan80',
	)


	return True


@app.route('/test')
def tester():
	return "Hello"

if __name__=='__main__':
	app.run(debug=True)
