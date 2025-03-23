import nbformat

with open('t1_simple_mnist_number_neural_network.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

with open('t1_simple_mnist_number_neural_network.ipynb', 'w', encoding='utf-8') as f:
    print("재직렬화함")
    nbformat.write(nb, f)
