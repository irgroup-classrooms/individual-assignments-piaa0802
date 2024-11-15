##Task 1

Colum: Counts the datasets 

char: The characters, which are currently speaking.

dialog: What the current character is saying.

movie: In which movie, the characters are saying the line.

##Task 2

###Using OenRefine

Step 1: All -> edit all columns -> Collapse consecutive whitespace

Step 2: All -> edit all columns -> Trim leading and trailing whitespace

Step 3: dialog -> Edit cells -> Transform -> value.replace(/^[,]+/, "")

Step 4: Repeat step 2

Step 5: Dialog -> Edit cells -> To titlecase

Step 6: Dialog -> Facet -> Facet by null -> All -> Edit rows -> Remove matching rows

Step 7: char -> Edit cells ->Transform -> value.replace("(", "")

Step 8: Dialog -> Facet -> Facet by empty string -> All -> Edit rows -> Remove matching rows

Step 9: Dialog -> Facet -> Create two facets: value.contains (")") and value.contains ("(") -> set both on true -> set one on false -> dialog -> Edit cells -> transform -> value.replace(")", "") -> set both facets on true again -> set the other one on false -> repeat process with transform -> value.replace("(", "") -> turn both on true again and check if they are now no single brackets anymore
