# lumiere-bio-task-1

One Lumiere task in the Biology domain. The figure is Figure 4 of a PLoS ONE paper which carries
a CC BY 4.0 licence, and the question asks how many mouse groups have a liver section free of
macrovesicular steatosis together with an AST to ALT ratio above 2. The answer is 2.

| File | What it holds |
|---|---|
| prompt.md | the prompt, the only text anybody pastes into the form |
| task.md | the form fields, the ground truth, the levers, the wrong answers |
| image.png | Figure 4 as the publisher serves it, 3483 x 4171, nothing changed |
| SOURCE.md | the citation, the licence and the md5 of the image |
| tools/decode_g004c.py | reads the ten bar values back out of the pixels |
| lumiere-bio-task-1.zip | all of the above in one file |
| feedback/ | one file per run, written after the models answer |

The task has not been run yet. Both models have to get it wrong before anything else gets
written, and if either one answers 2 the design is retired instead of submitted.
