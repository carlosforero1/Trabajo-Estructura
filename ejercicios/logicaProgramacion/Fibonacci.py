def fibonacci(n):
   ant = n
   actual = n
   result = [n]

   for i in range(5):
       temporal = actual +ant
       ant = actual
       actual = temporal
       result.append(actual)
   return result


if __name__ == '__main__':
    print(fibonacci(75))


