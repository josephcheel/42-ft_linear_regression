import argparse
import sys
import json

def estimateY(x=None, theta0=0.0, theta1=0.0) -> float:
	if theta0 == 0.0:
		print("Warning: that theta0 is set to default 0.0")
	if theta1 == 0.0:
		print("Warning: that theta1 is set to default 0.0")
	if x is None:
		raise ValueError("x is required")
	else:
		return (theta0 + (theta1 * x))

if __name__ == '__main__':
	argparser = argparse.ArgumentParser()
	argparser.add_argument("--x", help="Mileage", type=float)
	argparser.add_argument("--theta0", "-t0", help="Theta0", type=float, default=0.0)
	argparser.add_argument("--theta1", "-t1", help="Theta1", type=float, default=0.0)
	argparser.add_argument("--json", help="JSON file with thetas")

	args = argparser.parse_args()
	if args.x is None:
		try:
			tmp = input("Enter mileage: ")
			
			args.x = float(tmp)
			if args.x < 0:
				raise ValueError("Mileage must be a positive number.")
		except ValueError as e:
			print("Error:", e, file=sys.stderr)
			sys.exit(1)
	
	if args.json:
		try:
			with open(args.json, 'r') as f:
				data = json.load(f)
				args.theta0 = data['theta0']
				args.theta1 = data['theta1']
		except FileNotFoundError:
			print("Error: file not found", file=sys.stderr)
			sys.exit(1)
		except json.JSONDecodeError:
			print("Error: invalid JSON file", file=sys.stderr)
			sys.exit(1)
		except KeyError:
			print("Error: values theta0 and theta1 not found", file=sys.stderr)
			sys.exit(1)
	print(estimateY(args.x, args.theta0, args.theta1))
