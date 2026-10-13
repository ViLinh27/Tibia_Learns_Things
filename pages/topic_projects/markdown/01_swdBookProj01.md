# The Bank Statements Analyzer (Chapter 2)

## The Challenge

- Guy wants a piece of software that will automate the processing of his monthly bank statements so they're easy to
  get and not get overwhelmed.

## The Goal

1. Approach the problem in single class first

- See why this is bad and what we can learn from it

2. Learn Single Responsbility Principle

- help in code maintainability

3. Learn Cohesion and Coupling

## Bank Statements Analyzer Requirements

- The bank statements are given in CSV format
  - Date in day, month , year, amount spent, where spent
- Guy wants these queries answered
  - What is the total profit and loss from a list of bank statements?
    - Is it positive or negative?
  - How many bank transactions are there in a particular month?
  - What are his top 10 expenses?
  - What category does he spend most of his money on?

## KISS Principle

- Start with 1st query
  - Need to process CSV file and calculate sum of all amounts
  - this doesn't need to be complex
- KISS (Keep it short and sweet)
  - One single class is fine for just 1 query like in figure 2-1 on p 7.
- Exceptions won't need to be worried about until ch 3
  - what if file doesn't exist
  - what if parsing a loaded file didn't work

## --- Consider the Following ---

Not everyone separates their values by commas. They'll use different delimiters.

## --- Consider the Following ---

## Book Code

### Simple One Class Transaction Sum Calculator

Figure 2-1 on p7

```
public class BankTransactionAnalyzerSimple{
    private static final String RESOURCES = "src/main/resources/";

    public static void main(final String... args) throws IOException {
        final Path path = Paths.get(RESOURCES + args[0]);
        final List<String> lines = Files.readAllLines(path);

        double total = 0d;

        for(final String line: lines){
            final String[] columns = line.split(",");
            final double amount = Double.parseDouble(columns[1]);
            total += amount;
        }

        System.out.println("The total for all transactions is "+total);
    }
}
```

#### What's going on code above

1. Pass in csv file as a command line argument to app
2. Path class is path in file system basically
3. Use Files.readAllLines() to return list of lines
4. Parse all the lines one a time by:

- Splitting columns by columns
- Extracting amount
- Parsing amount to a double

5. Add the double to current total
6. Now you have total amount after all the looping through values

#### Consider

- The code works fine but misses corner cases
  - What if file is empty?
  - What if parsing amount failes because data was corrupted?
  - What if statement line has missing data?

#### Error when running the first project

I keep getting this error when running the compiled java class:

```
Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: Index 0 out of bounds for length 0
        at src.main.BankTransactionAnalyzerSimple.main(BankTransactionAnalyzerSimple.java:12)
```

What I had in the program was this:

```
public class BankTransactionAnalyzerSimple{
    private static final String RESOURCES = "src/main/resources/sample.csv";

    public static void main(final String... args) throws IOException {
        final Path path = Paths.get(RESOURCES + args[0]);
        final List<String> lines = Files.readAllLines(path);

        double total = 0d;

        for(final String line: lines){
            final String[] columns = line.split(",");
            final double amount = Double.parseDouble(columns[1]);
            total += amount;
        }

        System.out.println("The total for all transactions is "+total);
    }
}
```

Turns out that's not correct. The problem line was this:
`final Path path = Paths.get(RESOURCES + args[0]);`

`args` is basically an empty string. So `args[0]` is empty array when this is running. Hence the `ArrayIndexOutOfBoundsException` when this thing is running.

The way the code looks now the argument would looks like this since concatenation is happening (`final Path path = Paths.get(RESOURCES + args[0]);`):
`src/main/resources/sample.csvMyArgument`

The easiest way to get rid of the error is get rid of the + args[0] since unlike the book I'm calling the file directly
