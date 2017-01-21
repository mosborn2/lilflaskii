#payserver.py

import os
from flask import Flask, render_template, request
import stripe

print ("hello")

#establish stripe plan names here
plans = {
	'plan1',
	'plan2',
}

#grab api keys
stripe_keys = {
	'secret_key': os.environ['STRIPE_PRIVATE'],
	'publishable_key' : os.environ['STRIPE_PUBLIC'],
}

stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)

@app.route('/subscribe1', methods=['POST'])
def charge():

	customer = stripe.Customer.create(
		email='catsaregood@cats.com',
		source=request.form['stripeToken']
	)

	stripe.Subscription.create(
		customer=customer.id,
		plan=plans['plan1'],
	)


	return


@app.route('/test')
def tester():
	print ("hello")
	return

if __name__=='__main__':
	app.run(debug=True)
