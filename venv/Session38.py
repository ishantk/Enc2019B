from matplotlib import pyplot as plt
import numpy as np

# Activation Function
def sigmoid(inputs):
    # Output which sigmoid shall return as list
    outputs = []
    for x in inputs:
        cal = 1 / (1 + np.exp(-x))
        outputs.append(cal)
    return outputs

def softmax(inputs):
    outputs = np.exp(inputs) / sum(np.exp(inputs))
    return outputs

def hyperbolicTangent(inputs):
    outputs = np.tanh(inputs)
    return outputs


inputs = list(range(0, 21)) # 0 to 20
outputs = hyperbolicTangent(inputs)   # Returned from sigmoid function

print(inputs)
print(outputs)

plt.plot(inputs, outputs)
plt.xlabel("Inputs")
plt.ylabel("Outputs")
plt.show()