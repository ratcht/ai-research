from pysr import PySRRegressor

model = PySRRegressor(
  niterations=40,  # < Increase me for better results
  binary_operators=["+", "*", "-", "/", "^"],
  unary_operators=[
      "cos",
      "exp",
      "sin",
      "inv(x) = 1/x",
      "sqrt"
      # ^ Custom operator (julia syntax)
  ],
  extra_sympy_mappings={"inv": lambda x: 1 / x},
  # ^ Define operator for SymPy as well
  elementwise_loss="loss(prediction, target) = (prediction - target)^2",
  # ^ Custom loss function (julia syntax)
)

model.fit(X, y)
