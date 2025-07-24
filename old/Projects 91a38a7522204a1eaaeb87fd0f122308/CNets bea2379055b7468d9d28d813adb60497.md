# CNets

# Pointers

## Other examples

### Video #1

[https://www.youtube.com/watch?v=zt2Z8U_1kmw](https://www.youtube.com/watch?v=zt2Z8U_1kmw)

- The line `int a[][3] = {1, 2, 3, 4, 5, 6}` was confusing for me. When declaring arrays, the first time “`a[i][j]`” is written, it is a declaration of dimensions and not an access to its coordinates. Then, subsequent writings of “`a[i][j]`” are then accessing the array `a` at row `i` and column `j`.
- When you have a snippet like “`int *var[i]`”, a good advice is to read inside to outside, right to left. The order of operations is:
    - “`var`” a new variable, the variable name.
    - “`var[i]`” is read next, so `var` is an array of `i` elements.
    - “`*var[i]`" is next, so `var` is an array of `i` pointers.
    - “`int *var[i]`” finally say that `var` is an array of length `i` of pointers to integers.

## Practice (in `practice.c`)

### Solution #3

```c
void solution_3(int* iPtr, int* jPtr){

    // Write a C program to swap two numbers using pointers
    printf("Start: %d, %d\n", *iPtr, *jPtr);
	
    int* kPtr = iPtr; // incorrect from here
    *iPtr = *jPtr;
    *jPtr = *kPtr;

    printf("End: %d, %d\n", *iPtr, *jPtr);
}

void solution_3(int* iPtr, int* jPtr){

    // Write a C program to swap two numbers using pointers
    printf("Start: %d, %d\n", *iPtr, *jPtr);
	
    int k = *iPtr; // Correct solution
    *iPtr = *jPtr;
    *jPtr = k;

    printf("End: %d, %d\n", *iPtr, *jPtr);
}

int main() {

    int i = 2;
    int j = 5;
    int* iPtr = &i;
    int* jPtr = &j;

    solution_3(iPtr, jPtr);

    printf("Final; %d, %d\n", i, j);

    return 0;
}
```

### Solution #4

- In C, it’s not possible to determine the size of an array from a pointer alone because the pointer only holds the address of the first element.
- In C, it’s also not possible to return an array of anything from a function. You either pass  the array as a parameter and modify it inside the function, or you pass a pointer to the array.
- Maybe try a pointer to an array in the stack and not the heap ?

Two solutions.

- Solution #1:
    
    ```c
    int* solution4v1(size_t size) {
    
        // Write a C program to copy one array to another using pointers
        // Dynamically allocate memory for the array
        int* nums = (int*) malloc(size * sizeof(int));
    
        if (nums == NULL) {
            printf("Memory allocation failed\n");
            return NULL;
        }
    
        int currentNum;
        printf("Enter the numbers in the array: ");
        
        for (int* ptrNums = nums; ptrNums < nums + size; ptrNums++) {
            scanf("%d", &currentNum);
            *ptrNums = currentNum;
        }
    
        return nums;
    }
    
    int main() {
    
        size_t size = 4;
        int* solution = solution4v1(size);
    
        if (solution != NULL) {
            printf("Array elements are: ");
            for (size_t i = 0; i < size; i++) {
                printf("%d ", solution[i]);
            }
            printf("\n");
    
            // Free the allocated memory
            free(solution);
        }
    
        return 0;
    }
    ```
    
    **Pros:**
    
    - **Flexibility**: You can allocate large amounts of memory, limited only by the system’s available memory.
    - **Lifetime**: The memory remains allocated until you
    explicitly free it, which can be useful if you need the data to persist
    beyond the scope of the function.
    
    **Cons:**
    
    - **Manual Memory Management**: You need to remember to free the allocated memory to avoid memory leaks.
    - **Overhead**: Dynamic memory allocation can be slower and has some overhead compared to stack allocation.

- Solution #2
    
    ```c
    void solution4v2(int* nums, size_t size) {
        
        // Write a C program to copy one array to another using pointers
        
        int currentNum;
        printf("Enter the numbers in the array: ");
        
        for (int* ptrNums = nums; ptrNums < nums + size; ptrNums++) {
            scanf("%d", &currentNum);
            *ptrNums = currentNum;
        }
    }
    
    int main() {
        size_t size = 4;
        int nums[size];
    
        solution4v2(nums, size);
    
        printf("Array elements are: ");
        for (size_t i = 0; i < size; i++) {
            printf("%d ", nums[i]);
        }
        
        printf("\n");
    
        return 0;
    }
    ```
    
    **Pros:**
    
    - **Simplicity**: No need to manage memory manually; the stack memory is automatically managed.
    - **Speed**: Stack allocation is generally faster and has less overhead compared to heap allocation.
    
    **Cons:**
    
    - **Limited Size**: The stack has a limited size, so you can’t allocate very large arrays.
    - **Lifetime**: The memory is deallocated when the function returns, so the data won’t persist beyond the function’s scope.
- Arguments for which solution to choose:
    - **Use Solution 1 (Heap Allocation)** if you need to allocate large arrays or if the data needs to persist beyond the function’s scope.
    - **Use Solution 2 (Stack Allocation)** if the array size is small to moderate and you want simpler, faster memory management.

### Solution #5

- It is possible to make an assignment like `*(copy + i) = *(*base* + i);`, where the left-hand side contains an operation (which is a bit weird, but possible).
    
    ```c
    int* solution5(int* base, size_t size){
    
        // Write a C program to copy one array to another using pointers
    
        int* copy = (int*) malloc(size * sizeof(int));
    
        for (int i = 0; i < size; i++) {
            *(copy + i) = *(base + i);
        }
    
        return copy;
    }
    
    int main() {
    
        int base[3] = {1, 2, 3};
        int size = 3;
    
        int* copy = solution5(base, size);
        print_array(copy, size);
    
        return 0;
    }
    ```
    
- Another very pro function implementation would be like this:
    
    ```c
    void copy_array(int *source, int *destination, size_t size) {
        int *src_ptr = source;
        int *dest_ptr = destination;
        
        while (size--) {
            *dest_ptr++ = *src_ptr++;
        }
    }
    ```
    
    So, the order of operations is:
    
    1. `src_ptr` is evaluated (the value is read).
    2. `dest_ptr` is evaluated (the location to write to is determined).
    3. The value from step 1 is assigned to the location from step 2.
    4. `src_ptr` is incremented.
    5. `dest_ptr` is incremented.

### Solution #6

The problem that I had here was the signature: `void solution6(int** a, int** b)` , you need to remember that what’s passed inside the function is a copy, so whatever change you make to that copy, will be discarded at the end of the function.

However, if you pass *a pointer of a pointer*, and then you dereference to get the simple pointers, those simple pointers are not a copy but the real ones, **so changes made to them are preserved**.

A common pattern to modify in-place the contents of something (and not lose the changes) with a function is to take its pointer as a parameter, such that you can dereference it.

```c
void solution6Wrong(int* a, int* b){
    
    // Write a C program to swap two arrays using pointers

    int* c = a;
    a = b;
    b = c;

}

void solution6(int** a, int** b){
    
    // Write a C program to swap two arrays using pointers

    int* c = *a;
    *a = *b;
    *b = c;

}
```

Now, another problem was the main. You cannot do a declaration of a pointer and an assignment of an array like `*int** a*[]* = {1, 2, 3};` at the same time. Actually, what that is doing is declaring an array of pointers to integers (remember order of operations with “`type* var[]`” !

You need to do either :

- On the stack:
*`int* a*[]* = {1, 2, 3};
int* pa = a;` , careful, don’t do `*a` instead of `a`, `a` is already a pointer!
- On the heap:
`int *a *= (int*) malloc(3 * sizeof(int));
a[0] = 1;
a[1] = 2;
a[2] = 3;`

```c
int mainWrong() {

    int* a[] = {1, 2, 3};
    int* b[] = {4, 5, 6};

    solution6(&a, &b);

    print_array(a, 3);
    print_array(b, 3);

    return 0;
}

int main1() {

    int a[] = {1, 2, 3};
    int b[] = {4, 5, 6};

    int* pa = a; // WARNING: don't do *a
    int* pb = b; // WARNING: don't do *b

    solution6(&pa, &pb);

    print_array(pa, 3);
    print_array(pb, 3);

    return 0;
}

int main2() {

    int *a = malloc(2 * sizeof(int));
    int *b = malloc(2 * sizeof(int));
    
    a[0] = 1; a[1] = 2;
    b[0] = 3; b[1] = 4;

    solution6(&a, &b);
    print_array(a, 2);
    print_array(b, 2);

    free(a);
    free(b);
    
    return 0;
}
```

### Solution #7

No problem here really. Just don’t forget to check for `NULL` after `malloc`. Always.

```c
int* solution7(int* nums, int size){

    // Write a C program to reverse an array using pointers

    int* rev = (int*) malloc(size * sizeof(int));
    
    if (rev == NULL){
        return NULL;
    }
    
    for (int i = 0; i < size; i++){
        *(rev + i) = *(nums + size - i - 1);    
    }

    return rev;

}

int main() {
    int nums[] = {1, 2, 3, 4, 5};
    int size = sizeof(nums) / sizeof(nums[0]);

    printf("Original array: ");
    print_array(nums, size);

    int* reversed = solution7(nums, size);

    printf("Reversed array: ");
    print_array(reversed, size);

    // Free the dynamically allocated memory
    free(reversed);

    return 0;
}
```

### Solution #9

The problem that I had was in the function signature. Inside the arguments, I had “`int* matrix[3][3]`” but that reads as “an array of 3 arrays of 3 arrays of pointers to integers”. What we want is “`int (*matrix)[3]`” that reads “a pointer to an array of 3 integers”.

Actually, “`int (*matrix)[3]`” can also be “a pointer to an array of (unknown quantity of) arrays of 3 integers”. From `int (*matrix)[3]` alone, we can't tell if it's pointing to a single array of 3 integers or the first row of a larger 2D array. This ambiguity is actually a feature of C. Each pointer can point to a single integer, or it could point to the first integer of an array of any size.

- In C, when you pass a 2D array to a function, it decays to a pointer to its first row.
- This is why the same declaration `int (*nums)[3]` works for both a pointer to a single array of 3 integers and a pointer to the first row of a 2D array with 3 columns.

The distinction comes from how you use it:

```c
int array[3] = {1, 2, 3};
int (*p)[3] = &array;  // Points to a single array of 3 integers
											 // Notice the "&" to point to the whole array
											 // And not only the first element

int matrix[4][3] = {{1,2,3}, {4,5,6}, {7,8,9}, {10,11,12}};
int (*q)[3] = matrix;  // Points to the first row of a 2D array
											 // It points strictly to the first element
```

In practice, though, if we would have wanted a pointer to a simple array of 3 integers (that is, one row, not nested), we would only write in the signature “`int* matrix`”.

```c
int solution9(int (*matrix)[3], int row, int col){

    // Write a C program to access two dimensional array
    // using pointers

    return *(*(matrix + row - 1) + col - 1);
}

int main() {
    int matrix[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    int row = 2; // Example row (1-indexed)
    int col = 3; // Example column (1-indexed)

    int result = solution9(matrix, row, col);
    printf("Value at row %d, column %d: %d\n", row, col, result);

    return 0;
}
```

### Solution #10

Rien à noter.

```c
void solution10(int (*m1)[COLS], int (*m2)[COLS], int (*res)[COLS]){

    // Write a C program to add two 3x3 matrix using pointers

    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            *(*(res + i) + j) = *(*(m1 + i) + j) + *(*(m2 + i) + j);
        }
    }

}

int main() {
    int m1[ROWS][COLS] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    int m2[ROWS][COLS] = {
        {9, 8, 7},
        {6, 5, 4},
        {3, 2, 1}
    };

    int res[ROWS][COLS];

    solution10(m1, m2, res);

    printf("Resultant matrix:\n");
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            printf("%d ", res[i][j]);
        }
        printf("\n");
    }

    return 0;
}
```

### Solution #11 (Matrix mult.)

[solution11.txt](solution11.txt)

By the way, we define different matrices for `solution11v2` for them to work. 

---

- Instead of "`sizeof(*res)`", you can also write "`sizeof(int[COLS])`" or "`COLS * sizeof(int)`”.
- In C, there is no need to cast the output of malloc. The output of malloc is of type “`*void`”, and automatically detects what should be its type.

---

- With respect to pointer arithmetic and bracket-access syntax, the performance difference between them is typically negligible in modern compilers.
    - In C, bracket notation and pointer arithmetic are often interchangeable due to the language's design. However, there are some situations where you might need to use pointer arithmetic:
        - When working with void pointers: You can't use array indexing with void pointers, so you need to cast them or use pointer arithmetic.
        - In some low-level operations or hardware interfacing where you need precise control over address manipulation.
        - When dealing with complex pointer-to-pointer structures where the levels of indirection make bracket notation cumbersome or unclear.
        - In certain optimization scenarios where pointer arithmetic might be more efficient (though modern compilers often optimize array access to be equivalent).
        - When working with arrays of unknown size at compile time, especially in function parameters.
        - In some cases of pointer arithmetic involving structure members or when doing byte-level manipulations.

---

- When you declare an array like `int (*res)[COLS] = malloc(ROWS * sizeof(*res));`, you automatically declare the values in the array as `int*`. So, no need to re-declare “`int* res[i]`”.

When initializing `res`, when do we need to loop over its elements to initialize them?
    - Here, you're creating an array of pointers, where each pointer points to a separate array. This is often called a "jagged array" because each row can theoretically have a different length. Every row is allocated in a different part in the heap, **not contiguously**.
        
        ```c
        int** res = malloc(ROWS * sizeof(int*));
        for (int i = 0; i < ROWS; i++) {
            *(res + i) = malloc(COLS * sizeof(int));
        }
        ```
        
    - This allocates a **single contiguous block of memory** for the entire 2D array.
        
        ```c
        int (*res)[COLS] = malloc(ROWS * sizeof(*res));
        // No need to initialize the elements inside res.
        ```
        
    - Because we only need to initialize the contiguous block of memory once, we do not need to loop over its elements.
        
        

---

- **Important discovery.**
From "`int (*res)[COLS]`" we can't know if `res` points to a simple row or the first row of a matrix.
    - In practice, you tell the difference by the amount of bytes allocated in the heap. For a matrix (array of arrays), `int (*res)[COLS] = malloc(ROWS * sizeof(*res))`; for a simple array, `int (*res)[COLS] = malloc(sizeof(*res))`.
    - That said, C itself doesn't inherently "understand" or keep track of the dimensionality of the allocated memory based on the amount of bytes allocated. The type `int (*res)[COLS]` declares `res` as a pointer to an array of `COLS` integers, regardless of how much memory is actually allocated.
    - **Important**. If res is a simple row, you try to access `res[i][j]` where `i` is greater than 0, C will not prevent this or raise any error at compile time or runtime, even though you've only allocated memory for one row. The ability to use `res[i][j]` syntax comes from the type of `res`, not from the amount of memory allocated.
    - If `res` is declared as an array like “`int (*res)[COLS]`”, it is valid to write `res` (pointer to first element), `res[i]` and `res[i][k]`. Doing `res[i][j][k]` would return an error; you would need “`int (*res)[COLS][ROWS]`”. The same applies without passing through the pointer, i.e. “`int res[COLS]`”.
    - It's important to note that when you declare an array like `int res[ROWS][COLS]`, you're allocating the entire 2D array on the stack (or in static memory if it's a global variable). When you use `int (*res)[COLS]`, you're just declaring a pointer, which can then point to dynamically allocated memory on the heap (using malloc) or to an existing array.

### Solution #12

## In “`Matrix`” structure

Our Matrix structure is as follows :

```c
typedef struct {
    size_t rows;
    size_t cols;
    float** data;
} Matrix;
```

- An “array of pointers to arrays” is different than an “standard 2D array”. From the “`float** data`” statement, we cannot know if data is going to be one or another. That decision is rather done at the moment of assignment and not at the moment of declaration.
    - If it were to be an array of pointers to arrays:
        
        ```c
        // Allocation
        float** data = (float**)malloc(rows * sizeof(float*));
        for (size_t i = 0; i < rows; i++) {
            data[i] = (float*)malloc(cols * sizeof(float));
        }
        
        // Memory layout
        data --→ [ptr][ptr][ptr]...
                  ↓    ↓    ↓
                 [f][f][f]  [f][f][f]  [f][f][f]...
        
        // Freeing
        for (size_t i = 0; i < rows; i++) {
            free(data[i]);
        }
        free(data);
        ```
        
    - If it were to be an standard 2D array:
        
        ```c
        // Allocation
        float (*data)[cols] = malloc(rows * cols * sizeof(float));
        
        // Memory layout
        data --→ [f][f][f][f][f][f][f][f][f]...
                 (contiguous block of rows * cols floats)
        
        // Freeing
        free(data);
        ```
        
    - Key differences:
        1. Allocation:
            - Array of pointers: Requires multiple allocations (one for the array of pointers, one for each row).
            - True 2D array: Single allocation for the entire block.
        2. Memory layout:
            - Array of pointers: Non-contiguous. Each row can be in a different part of memory.
            - True 2D array: Contiguous block of memory.
        3. Accessing elements:
            - Array of pointers: `data[i][j]`
            - True 2D array: `data[i][j]` or `(*(data + i) + j)`
        4. Freeing:
            - Array of pointers: Requires a loop to free each row, then free t8he array of pointers.
            - True 2D array: Single free operation.
        5. Flexibility:
            - Array of pointers: Can have rows of different lengths (jagged array).
            - True 2D array: All rows must have the same length.
        
        In the neural network code, the array of pointers approach is used, which allows for more flexibility in memory management but requires more complex allocation and deallocation processes.
        
- In short, if it is a array of pointers to arrays (row-major order), you need to free the innermost pointers, i.e the rows (`data[i]`). With that, you are also freeing the floats contained in that row.