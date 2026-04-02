def add_binary(a, b):
    a = a[2:]
    b = b[2:]   

    i = len(a) - 1
    j = len(b) - 1
    
    carry = 0
    result = ""
    
    while i >= 0 or j >= 0 or carry > 0:
        total = carry
        
        if i >= 0:
            if a[i] == '1':
                total += 1
            i -= 1
            
        if j >= 0:
            if b[j] == '1':
                total += 1
            j -= 1
            
        result = str(total % 2) + result
        
        carry = total // 2
        
    result = result.lstrip("0")
    
    if result == "":
        result = "0"
        
    return "0b" + result
