[Tensor Flow install](https://www.tensorflow.org/versions/r0.11/get_started/os_setup.html#pip-installation)

Installation location: /home/commander/.virtualenvs/tensorclassy/lib/python3.4/site-packages/tensorflow

Okay, to implement:
* create virtual environment for python3: <code>mkvirtualenv --pytho=/usr/bin/python3 tfic</code>
* pip install tensfor flow: [instructions here](https://www.tensorflow.org/versions/r0.11/get_started/os_setup.html#pip-installation)
* run built-in method <code>maybe_download_and_extract()<code> to download ImageNet:

<pre><code>import tfic
tfic.maybe_download_and_extract()
</code></pre>

Use:
<pre><code>import tfic
results = tfic.run_inference_on_image(IMAGE_URL)
</code></pre>





