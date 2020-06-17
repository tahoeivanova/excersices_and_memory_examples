def list_trick(a, list_test = []):
    list_test.append(a)
    return list_test

def list_trick_2(a=[], list_test = []):
    list_test.append(a)
    return list_test

if __name__ == '__main__':

    a = 1
    func_result = list_trick(a)
    print(func_result)
    func_result_1 = list_trick(a)
    print(func_result_1)
    print(func_result is func_result_1)
    func_result = list_trick(a, [500,600,700])
    print(func_result)
    func_result_1 = list_trick(a, [500,600,700])
    print(func_result)
    print(func_result is func_result_1)


    a = [1,2,3]
    func_result = list_trick(a)
    print(func_result)
    func_result_1 = list_trick(a)
    print(func_result_1)
    print(func_result is func_result_1)
    func_result = list_trick(a, [500,600,700])
    print(func_result)
    func_result_1 = list_trick(a, [500,600,700])
    print(func_result)
    print(func_result is func_result_1)
