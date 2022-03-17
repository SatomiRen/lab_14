#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sample(string):
    def name_surname(n, s):
        sample_data = string.replace("%N%", n)
        sample_data = sample_data.replace("%F%", s)
        return sample_data

    return name_surname


if __name__ == "__main__":
    sample_string = (
         "Greetings %F% %N%! You are doing the function closure."
    )
    name, surname = input("Enter your name and surname: ").split()
    print(sample(sample_string)(name, surname))
