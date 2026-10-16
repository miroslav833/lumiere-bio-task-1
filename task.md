# Current attempt: 1 (liver histology plus serum transaminases, count of groups)

Status: NOT YET RUN.

Instructions for the extension run:

1. Read the form table below, fill it in, upload image.png, paste the prompt under
   "## Step 4. Prompt" exactly as written.
2. Tick boxes 1, 3, 4. Leave box 2 for Miroslav.
3. Wait for both model blocks, log them as feedback/001.md: expected answer, verdict, checker
   findings, Block 1 raw, Block 2 raw with reasoning.
4. Both must be wrong. If either answers 2, stop and report. Steps 7 to 11 are written only
   after both fail. Do not press submit.

| Field | Value |
|---|---|
| Subdomain | Cell/Molecular Biology |
| Where did the image(s) come from | External - open-access |
| Source URL or DOI | https://doi.org/10.1371/journal.pone.0173975 |
| License | CC BY 4.0 |
| Reference material | A wild-type mouse-based model for the regression of inflammation in atherosclerosis |
| Publication venue | PLoS ONE 12(3): e0173975, 14 March 2017 |
| Image | image.png, Figure 4 of that article, 3483 x 4171, unmodified |

Attribution line for the form if one is asked for: Peled M, Nishi H, Weinstock A, Barrett TJ,
Zhou F, Quezada A, Fisher EA (2017) PLoS ONE 12(3): e0173975, Figure 4, CC BY 4.0.

---

## Step 4. Prompt

Image 1 has two panels from a mouse study of diet-induced liver change. Panel A shows haematoxylin and eosin stained liver sections from five groups of mice, each group labelled above its own section. Panel B shows the mean serum aspartate aminotransferase and the mean serum alanine aminotransferase of the same five groups, with the group names on the horizontal axis and the enzyme identity in the legend.

Count the groups which meet both of the conditions below, and report that count.

Condition one is histological. The liver section of the group shows no macrovesicular steatosis. A section counts as steatotic when large round clear vacuoles fill most of the hepatocytes across the whole field. Isolated clear spaces which are vessel lumens or bile ducts are not steatosis, and a section with only those counts as free of steatosis.

Condition two is biochemical. The ratio of mean aspartate aminotransferase to mean alanine aminotransferase for that group is greater than 2. Read each bar to the nearest 10 U/L, use the bar top and not the top of the error bar, and treat the values read that way as exact.

Report your final answer as a single integer, with no units and no further text.

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

Checker note: NON_FOUNDATIONAL_REFERENCE is a known false positive on every image task. Record
it and continue. Rebuttal text is in the playbook under task-pass-experience section 4.

---

## Ground truth

Ten bar readings and five histology calls. Values below were measured from the pixels of
image.png with tools/decode_g004c.py, using the y axis ticks at 0, 100, 200, 300, 400 and
500 U/L, which sit 167.1 pixel rows apart.

| group | AST U/L | ALT U/L | AST/ALT | section | counts |
|---|---|---|---|---|---|
| Base-line | 262 | 264 | 0.99 | steatotic | no |
| Chow regression | 209 | 47 | 4.48 | clean | yes |
| MTPi regression | 275 | 44 | 6.20 | clean | yes |
| Progression | 247 | 249 | 0.99 | steatotic | no |
| Western only | 340 | 319 | 1.06 | steatotic | no |

Two groups meet both conditions, so the answer is 2.

Read to the nearest 10 U/L the ratios are 210/50 = 4.2 and 270/40 = 6.75, both still above 2,
and the three steatotic groups sit at 0.98, 0.99 and 1.06, all far below 2. The threshold of 2
has no group anywhere near it, so the count does not move with reading error.

Panel A, what each section shows:
- Base-line, upper left. Large clear round vacuoles across the entire field, most hepatocytes
  affected. Steatotic.
- Chow regression, upper right. Uniform eosinophilic hepatocyte cords. Three or four clear
  spaces which are a central vein and portal tracts, plus one dark basophilic focus. No vacuoles
  in the hepatocytes. Clean.
- MTPi regression, middle left. Same picture as chow regression, five clear vessel lumens of
  varying size scattered through an otherwise solid field. Clean.
- Progression, middle right. Vacuoles across the whole field, same as base-line. Steatotic.
- Western only, lower left. Vacuoles across the whole field, the coarsest of the five.
  Steatotic.

## Where the levers are

1. The two clean sections are not empty. Each carries several large white spaces which are
   vessel lumens, and in a thumbnail they read as lipid droplets. Calling either section
   steatotic drops the count to 1 or 0. This is the signal versus artifact failure mode the
   Biology guide lists, and it is built into the image rather than added to it.
2. Panel B has two series and the legend is the only thing which says which is which. Swapping
   aspartate aminotransferase for alanine aminotransferase inverts both ratios of interest to
   0.22 and 0.16 and gives a count of 0.
3. Every bar carries an error bar whose cap sits well above the bar top. Reading the cap instead
   of the bar lifts base-line to about 310 and chow to about 250, which does not change the
   count, so this one is a distraction rather than a trap. The prompt rules it out anyway.
4. The answer needs all five sections classified and all ten bars read. One misclassification
   moves the count.

## Wrong answers and what they encode

| answer | error it encodes |
|---|---|
| 0 | both clean sections read as steatotic, vessel lumens taken for lipid droplets |
| 1 | one of the two clean sections read as steatotic |
| 3 | the Western only section read as clean, or the ratio condition dropped |
| 4 | the ratio condition applied to the wrong series, or ignored |
| 5 | both conditions ignored, every group counted |

## Why this design

Every numeric readout in this figure sits on an axis with ticks every 100 U/L and no minor
gridlines, so no three significant figure answer can be defended from it. The count is the
quantity the figure can carry exactly. The histology call is the part a model has to get right
from pixels, and the ratio test is what stops the count being a bare tally.
