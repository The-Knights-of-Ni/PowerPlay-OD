import tensorflow as tf

# Darknet cells
class DarknetBlock(tf.keras.Model):
	def __init__(self, filters):
		super().__init__()

		# Layer for conv 1x1
		self.one_conv2d = tf.keras.layers.Conv2D(filters, 1, 1, padding="same")
		self.batchnorm1 = tf.keras.layers.BatchNormalization()
		# Layer for conv 3x3
		self.three_conv2d = tf.keras.layers.Conv2D(filters*2, 3, 1, padding="same")
		self.batchnorm2 = tf.keras.layers.BatchNormalization()

	def call(self, input_tensor, training=False):
		# Calculate the stuff
		# The conv stuff 1x1
		x = self.one_conv2d(nput_tensor)
		x = self.batchnorm1(x, training=training)
		x = tf.nn.leaky_relu(x, alpha=0.1)

		# The conv 3x3 stuff
		x = self.three_conv2d(x)
		x = self.batchnorm2(x, training=training)
		x = tf.nn.leaky_relu(x, alpha=0.1)

		# The stuff for residual connections
		x += input_tensor

		return x

# Make main model
def create_yolov3():
	# TODO
