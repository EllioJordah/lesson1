
def get_summ(one, two, delimiter='&'):
    one=str(one)
    two=str(two)
    c=f'{one}{delimiter}{two}'
    return c
result=get_summ('learn','python')
print(result.upper())
