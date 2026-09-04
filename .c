

 #include <stdio.h>

int main() {
    float num1, num2, result;
    char operator;

    printf("Enter first number: ");
    scanf("%f", &num1);

    printf("Enter operator (+, -, *, /): ");
    scanf(" %c", &operator);

    printf("Enter second number: ");
    scanf("%f", &num2);

    if (operator == '+') {
        result = num1 + num2;
    }
    else if (operator == '-') {
        result = num1 - num2;
    }
    else if (operator == '*') {
        result = num1 * num2;
    }
}else if (operator == '/') {
        if (num2 != 0) {
            result = num1 / num2;
        }
        else {
            printf("Cannot divide by zero.");
            return 0;
        }
    }
    else {
        printf("Invalid operator.");
        return 0;
    }

    printf("Result = %.2f\n", result);

    return 0;
}