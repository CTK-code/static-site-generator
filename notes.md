# Project Notes

## Chapter 3 Lesson 1
#### Jan 17 2025

The goal of this is to split text nodes into smaller pieces, breaking them down into their 
individual components of **BOLD**, *italic* and `code` text nodes.

### Initial plan:

Split the string based on the delimiter. Then grab every second grouping of text as that would be the block of the
desired TextType. I do not think that this will work with nesting, but it probably doesnt have to as I could just keep 
calling the method as long as a *, ** or ` is contained. This will breakdown with single chars but that might be a 
futur problem. 

I have already written a suite of unit tests that should allow for proper testing of single nesting, but not double.

### Questions/problem
The description says that the order that the delimiters will be checked is importanta and that
that will simplify the implementation, but I do not know how that could be as to be the breakdown *should* work with the
split on delim method. Except that ** includes * so... Have to come up with a plan for that. But that means if I am looking for \*\*
then I can ignore the \*, just not the other way around.
