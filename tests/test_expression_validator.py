from expression_validator.validator import valid_expression

def test_happy():
    assert valid_expression('([{Hello}])')

def test_close_before_open():
    assert not valid_expression(')[]{}')

def test_not_closing():
    assert not valid_expression('[]({}')

def test_not_interlaced():
    assert not valid_expression('{[(])}')

def test_without_brackets():
    assert valid_expression('abcde')

def test_empty_string():
    assert valid_expression('')