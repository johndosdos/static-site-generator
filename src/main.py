from process_nodes import *


def main():
    markdown = """# This is a level 1 heading

## This is a level 2 heading

### This is a level 3 heading

#### This is a level 4 heading

##### This is a level 5 heading

###### This is a level 6 heading

``` This is a code block ```

```
This is also a code block
```

> This is a quote block

- This is an
- Unordered list

1. This is an
2. Ordered list

This is a paragraph."""

    result = markdown_to_htmlnode(markdown)
    return result


main()
