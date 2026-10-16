# Biology task 1, attempt 1: liver sections and serum transaminases

Status: NOT YET RUN.

How to run it. Fill the form from the table below, upload image.png, and paste the prompt from
prompt.md word for word, because prompt.md is the copy which was humanized and checked. Tick
boxes 1, 3 and 4, and leave box 2 for Miroslav. Wait for both model blocks, then save them as
feedback/001.md with the expected answer, the verdict, any checker findings, and both blocks in
full including their reasoning. Both blocks have to be wrong, so if either one answers 2 the run
is over and nothing gets submitted. Steps 7 to 11 are written only after both of them fail.

| Field | Value |
|---|---|
| Subdomain | Immunology |
| Where did the image(s) come from | External - open-access |
| Source URL or DOI | https://doi.org/10.1371/journal.pone.0173975 |
| License | CC BY 4.0 |
| Reference material | A wild-type mouse-based model for the regression of inflammation in atherosclerosis |
| Publication venue | PLoS ONE 12(3): e0173975, 14 March 2017 |
| Image | image.png, Figure 4 of that article, 3483 x 4171, nothing changed |

If the form asks for an attribution line, use this one. Peled M, Nishi H, Weinstock A,
Barrett TJ, Zhou F, Quezada A, Fisher EA (2017) PLoS ONE 12(3): e0173975, Figure 4, CC BY 4.0.

---

## Step 4. Prompt

The prompt lives in prompt.md so that one file is the only thing anybody copies. Paste that file
and nothing else.

---

## Step 6. GTFA

2

---

## Checkboxes

| Statement | Answer |
|---|---|
| I've double checked my spelling and grammar. | True |
| My prompt is not duplicative, plagiarized, or LLM-generated. | Box 2 is Miroslav's, leave it |
| My prompt is self-contained and fully solvable without external resources. | True |
| The prompt can only be solved with the information in the image. | True |

NON_FOUNDATIONAL_REFERENCE fires on every image task because the checker reads the prompt
without the attachment, so record it and carry on. The rebuttal wording sits in the playbook
under task-pass-experience section 4.

---

## Ground truth

The answer rests on ten bar readings and five calls on the sections. Every number below came out
of the pixels of image.png with tools/decode_g004c.py, which calibrates against the y axis ticks
at 0, 100, 200, 300, 400 and 500 U/L, and those ticks sit 167.1 pixel rows apart.

| group | AST U/L | ALT U/L | AST/ALT | section | counts |
|---|---|---|---|---|---|
| Base-line | 262 | 264 | 0.99 | steatotic | no |
| Chow regression | 209 | 47 | 4.48 | clean | yes |
| MTPi regression | 275 | 44 | 6.20 | clean | yes |
| Progression | 247 | 249 | 0.99 | steatotic | no |
| Western only | 340 | 319 | 1.06 | steatotic | no |

Two groups clear both conditions, so the answer is 2.

The prompt asks for a reading by eye against ticks which stand 100 U/L apart, and the count
survives that. Rounding every bar to the nearest 25 U/L gives ratios of 4.00, 5.50, 0.91, 1.00
and 1.08, and rounding to the nearest 50 U/L gives 4.00, 6.00, 1.00, 1.00 and 1.17. The two
qualifying groups stay far above the threshold of 2 under both, and the three steatotic groups
stay near 1, so no plausible misreading of a bar moves the answer.

The checker raised three findings on the first wording and all three were taken. It called the
old closing line open ended, so the prompt now asks for the call on each section and the values
read before the integer. It called "most of the hepatocytes" soft, so the rule is now more than
half of the hepatocytes in the field. It pointed out that a reading to the nearest 10 U/L is
finer than an axis ticked every 100 U/L can support, which is right, so the prompt now asks for
a reading by eye against those ticks.

What each section in panel A actually shows:

- Base-line, upper left. Large round clear vacuoles over the entire field with most hepatocytes
  taken up by them, so the section is steatotic.
- Chow regression, upper right. Even eosinophilic hepatocyte cords, with three or four clear
  spaces which are a central vein and portal tracts, and one dark basophilic focus. The
  hepatocytes themselves carry no vacuoles, so the section is clean.
- MTPi regression, middle left. The same picture as chow regression, where five vessel lumens of
  different sizes are scattered through a field which is otherwise solid, so the section is clean.
- Progression, middle right. Vacuoles over the whole field in the same way as base-line, so the
  section is steatotic.
- Western only, lower left. Vacuoles over the whole field and the coarsest of the five, so the
  section is steatotic.

## Where the levers are

The two clean sections are not blank, and that is the whole trap. Each of them carries several
large white spaces which are vessel lumens, and at thumbnail size those spaces read as fat
droplets, so a model which calls either section steatotic drops the count to 1 or to 0. The
Biology guide lists signal versus artifact as a failure mode to aim at, and here it already sits
in the image instead of being added to it.

Panel B carries two series and only the legend says which is which, so a model which swaps
aspartate aminotransferase for alanine aminotransferase turns the two ratios that matter into
0.22 and 0.16 and reports a count of 0.

Every bar carries an error bar whose cap stands well above the top of the bar. Reading the cap
lifts base-line to about 310 and chow regression to about 250, neither of which moves the count,
so this one is a distraction rather than a trap, and the prompt rules it out anyway.

All five sections have to be classified and all ten bars have to be read before the count comes
out, so one wrong call anywhere moves the answer.

## Wrong answers and what each one means

| answer | what the model did |
|---|---|
| 0 | read both clean sections as steatotic and took vessel lumens for fat droplets |
| 1 | read one of the two clean sections as steatotic |
| 3 | read the Western only section as clean, or dropped the ratio condition |
| 4 | applied the ratio condition to the wrong series, or ignored it |
| 5 | ignored both conditions and counted every group |

## Why the answer is a count and not a measurement

Every number in this figure sits on an axis with ticks every 100 U/L and no minor gridlines
between them, so no three significant figure answer can be defended from it and a reviewer with
a straight edge would not get one either. A count is the quantity this figure can carry exactly.
The call on the sections is the part a model has to earn from the pixels, and the ratio test is
what keeps the count from being a bare tally.
