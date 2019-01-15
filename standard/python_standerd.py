#


def foo(x, y, name="bar"):
    """Computes foo.

    Given two 1-D tensors `x` and `y`, this operation computes the foo.

    Example:

    ```
    # x is [1, 1]
    # y is [2, 2]
    tf.foo(x, y) ==> [3, 3]
    ```
    Args:
    x: A `Tensor` of type `int32`.
    y: A `Tensor` of type `int32`.
    name: A name for the operation (optional).

    Returns:
    A `Tensor` of type `int32` that is the foo of `x` and `y`.

    Raises:
    ValueError: If `x` or `y` are not of type `int32`.
    """