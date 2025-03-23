# Problem 4. Discounted Dough-lers and Crustworthy Counts

Your shift is almost over, but the final stretch is always the trickiest. Just when you think you're done, the register flashes an ominous "DISCOUNT APPLIED" message, and suddenly, you're knee-deep in math.

The arcade pizzeria is famous for its outrageous deals—group discounts, special day discounts, discounts on top of discounts. At this point, you're half convinced someone is just making these up on the spot. Your task? Make sure each party pays the right amount, stacks the correct discounts, and splits their bills fairly without anyone throwing pepperoni at you.

And just when you think you're free, your manager slaps a clipboard into your hands. “Inventory check.”

Nothing strikes fear into a pizza worker’s heart quite like an end-of-shift ingredient count. Too many pineapples? Suspicious. Not enough cheese? Someone’s getting interrogated. If the numbers don’t add up, you’ll be stuck here recalculating while your coworkers escape into the night. Better make it quick—before they decide you’re the reason for the missing ham.

# The Tasks
## Part A: Calculate Earnings

The price of 1/8 of a pizza is $3. Given the total number of pizzas delivered, calculate the total amount of earnings.

*Input Details*:
- total_pizzas: total number of pizzas delivered

*Task*:
- Return the total amount of earnings (as an int)

## Part B: Apply Group Discounts
The arcade offers group discounts based on party size:
- 4 people → $5 discount
- 6 people → $8 discount
- 8 people → $14 discount

*Input Details*:
- You will receive a list of lists, where each inner list represents a party of people.
- Each party contains a list of numbers, where each number represents the amount of pizza an individual ate.
- These numbers will always be multiples of ⅛ in their simplest form.

*Discount Rules*:
- A party doesn’t need to have exactly 4, 6, or 8 people to qualify—they just need at least that many.
- Discounts stack starting from the greatest discount first. For example, a 13-person party would receive the 8-person discount first, then the remaining 5 people of the party would qualify for the 4-person discount.

*Task*:
- First, calculate the total cost of the party based on the amount of pizza eaten.
- Apply the largest applicable discount(s) for each party (discounts stack from largest to smallest).
- Return a list of integers, where each integer represents the final total cost for the corresponding party after all discounts are applied.

## Part C: Apply Day Discounts & Split the Bill
The arcade pizzeria is super generous and also has discounts on certain days!
- Sunday → 25% off
- Wednesday → 15% off
- Friday → 20% off

Given the total cost for each party (calculated in Part B), apply these day-specific discounts on top of any group discounts. After applying the discount for the specific day, each person in the party will pay separately. (You don't have to call anything from Part B, assume group discounts have been calculated already.) 

Input Details:
- A list of lists, where each inner list represents a party, and each number in that list is the amount of pizza an individual ate.
- A list of total party costs, where each value corresponds to the party’s total cost after group discounts (from Part B).

*Task*:
- Apply the appropriate day discount to each party’s total cost.
- Split the discounted total fairly among the party based on the proportion of pizza each person ate.
- Return a dictionary, where:
    - The keys are the discounted days ("Sunday", "Wednesday", "Friday").

The values are lists of lists, where each inner list contains the final cost per person after all discounts, rounded to two decimal places.
Formatting Hint: don’t worry about the returning costs for each person being a specific format. Just round to 2 decimal places (e.g. if cost is something like 0, 4, or 1.2 it would end up being 0.0, 4.0, and 1.2 because round() returns floats.)

**Sample Input**: problem_4c([[½, ¼, ⅛ ], [¼, ⅝, ½, ½ ]], [21, 40])

**Sample Output**:
    {‘Sunday’ : [[11.57, 5.79, 2.89], [4.0, 10.0, 8.0, 8.0]], 
    ‘Wednesday’ : [[13.11, 6.56, 3.28], [4.53, 11.33, 9.07, 9.07]], 
    ‘Friday’ : [[12.34, 6.17, 3.09], [4.27, 10.67, 8.53, 8.53]]}

## Part D: Ingredient Inventory
Before your shift ends, make sure that all the ingredients are accounted for!

Write a function that returns a table as a string showing the before and after amounts of each ingredient.

You will be given the total amount of ingredients at the start of the day. 

Based on the number of pizza slices sold, calculate how much of each ingredient remains.

An ingredient entry from the table should look like this: 

`Name of Ingredient | Before: (original amount) | After: (amount left over)`

**Sample Output**: 

`Pepperoni | Before: 402 | After: 305`

`Bacon | Before: 4 | After: 0`

*Make sure the formatting matches exactly! Each ingredient should be on a separate line.*

- Each pizza slice takes the following number of ingredients:
    - 6 Pepperonis
    - 4 Mushrooms 
    - 2 Bacons
    - 4 Pineapples
    - 5 Olives
    - 1 Ham
    - 3 Peppers
    - 4 Onions
    - 6 Sausages
    - 0.1 lbs cheese
        - For some reason, the inventory tracker is configured to only accept kilograms (kgs) for the amount of cheese in the inventory. There is a low-priority ticket to get that fixed, but for now please convert to kilograms in your output and round to the nearest whole number.

- The total amount of ingredients before the day started:
    - 402 Pepperonis
    - 293 Mushrooms
    - 251 Bacons
    - 620 Pineapples
    - 582 Olives
    - 152 Ham
    - 487 Peppers
    - 124 Onions
    - 591 Sausages
    - 10 kgs Cheese


[Get started with the starter code: problem4a.py](https://github.com/audreyyluu/icssc-brain-games-blindfolded-coding-2025/blob/main/problem4a.py)

[Get started with the starter code: problem4b.py](https://github.com/audreyyluu/icssc-brain-games-blindfolded-coding-2025/blob/main/problem4b.py)

[Get started with the starter code: problem4c.py](https://github.com/audreyyluu/icssc-brain-games-blindfolded-coding-2025/blob/main/problem4c.py)

[Get started with the starter code: problem4d.py](https://github.com/audreyyluu/icssc-brain-games-blindfolded-coding-2025/blob/main/problem4d.py)
