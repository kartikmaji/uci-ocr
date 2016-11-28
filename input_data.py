"""Functions for downloading and reading UCI data."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import gzip
import os
import tempfile

import numpy
from six.moves import urllib
from six.moves import xrange  # pylint: disable=redefined-builtin
import tensorflow as tf
from tensorflow.contrib.learn.python.learn.datasets.uci import read_data_sets

size = 64

def convert(outf, n):
    o = open(outf, "rb")

    images = []

    for i in range(n):
        image = [ord(o.read(1))]
        for j in range(8*8):
            image.append(ord(o.read(1)))
        images.append(image)

    o.close()

size = 784
convert("uci_data_testing.csv", 1000)
convert("uci_data_training.csv", 4620)

