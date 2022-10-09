import tensorflow as tf

# Darknet cells
class DarknetBlock(tf.keras.Model):
	def __init__(self, stride, filters):
		super().__init__()

		# Layer for depthwise convolution
		self.depth_conv2d = tf.keras.layers.DepthwiseConv2D(3, stride)
		self.batchnorm1 = tf.keras.layers.BatchNormalization()
		# Layer for 1x1 convolution
		self.one_conv2d = tf.keras.layers.Conv2D(filters, 1)
		self.batchnorm2 = tf.keras.layers.BatchNormalization()
		# Layer for depthwise concatenation
		self.concat = tf.keras.layers.Concatenate()

	def call(self, input_tensor, training=False):
		# Calculate the stuff
		# The depth stuff
		x = self.depth_conv2d(input_tensor)
		x = self.batchnorm1(x, training=training)
		x = tf.nn.leaky_relu(x, alpha=0.1)

		# The conv stuff 1x1
		x = self.one_conv2d(x)
		x = self.batchnorm2(x, training=training)

		# The stuff for residual connections
		x += input_tensor

		return tf.nn.leaky_relu(x, alpha=0.1)
