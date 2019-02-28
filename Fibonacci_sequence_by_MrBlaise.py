#!/usr/bin/env python3

# Fibonacci Sequence Generator
# Have the user enter a number and generate a fibonacci sequence
# which size is equivalent to that number.


def fibSequence(n):
    """
    Generates a fibonacci sequence with the size of n
    """
    assert n > 0 #basically prepares to thrown an exception if disproven

    series = [1] #starts w/list of single item

    while len(series) < n: #good use case of 'while' here (unknown duration)
        if len(series) == 1:
            series.append(1) 
        else:
            series.append(series[-1] + series[-2]) #append the last and 2nd-to-last

    for i in range(len(series)):  # Convert the numbers to strings (but why...?)
        series[i] = str(series[i])

    return(', '.join(series))   # Return the sequence seperated by commas
                                # useful: can wrap .join items in characters

def main():     # Wrapper function

    print(fibSequence(int(input('How many numbers do you need? '))))

if __name__ == '__main__': # need to research this more
    main()