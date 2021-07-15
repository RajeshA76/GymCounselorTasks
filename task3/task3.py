import pandas as pd

input = {'dates':['05Sep2009','13Sep2011','21Sep2010']}


def df_convert(input):
	"""Converting datetime to the format %d%b%Y using pandas datetime function"""
	df = pd.DataFrame(input)
	print("*****************")
	print("Before formatting")
	print("*****************")
	print(df)

	df['dates'] = pd.to_datetime(df.dates,format="%d%b%Y")
	print("****************")
	print("After formatting")
	print("****************")
	print(df)


df_convert(input)
