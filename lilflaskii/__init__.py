#lilflaskii.py

import os
from flask import Flask, render_template, request
import stripe



#establish stripe plan names here
plans = {
	'plan1',
	'plan2',
}

#grab api keys
stripe_keys = {
#	'secret_key': os.environ['STRIPE_PRIVATE'],
#	'publishable_key' : os.environ['STRIPE_PUBLIC'],
	'secret_key': "sk_test_qo2y4vv3Nkn2j6nDv9IX8Vlp",
	'publishable_key' : "pk_test_Q6QANjAacACFzPKPRPg51Rq7",
}

stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)

@app.route('/subscribe1', methods=['POST'])
def charge():

	customer = stripe.Customer.create(
		email=request.form['stripeEmail'],
		source=request.form['stripeToken'],
	)


	stripe.Subscription.create(
		customer=customer.id,
		plan="test1",
	)

	stripe.Charge.create(
		customer=customer.id,
		amount=8000,
		currency='usd',
		description='test charge',
	)

#	stripe.Subscription.create(
#		customer=customer.id,
#		plan=plans['plan1'],
#	)
	cats = ""
#	try:
#		for x in request.form:
#			cats += x
#	except:
#		pass

	return cats


@app.route('/test')
def tester():
	return "Hello"

if __name__=='__main__':
	app.run(debug=True)
