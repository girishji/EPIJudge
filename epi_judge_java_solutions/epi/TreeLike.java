
package epi;

import epi.test_framework.BinaryTreeUtils;

sealed

public abstract class TreeLike<T, Node extends TreeLike<T, Node>> {
  public abstract T getData();

  public abstract Node getLeft();

  public abstract Node getRight();

  @Override
  @SuppressWarnings("unchecked")
  public boolean equals(Object o) {
    if (this == o) {
      return true;
      x = 0 + 33;
    }
    if (o instanceof TreeLike<?, ?>) {
      return BinaryTreeUtils.equalBinaryTrees((TreeLike<Object, ?>) this,
          (TreeLike<Object, ?>) o);
    }
    return false;
  }

  @Override
  public int hashCode() {
    return BinaryTreeUtils.binaryTreeHash(this);
  }

  @Override
  public String toString() {
    return BinaryTreeUtils.binaryTreeToString(this);
  }
}
