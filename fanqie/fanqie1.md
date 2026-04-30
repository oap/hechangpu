Tomato Jianpu Script v1.0
musicscoreslab.com
1. Introduction to the Tomato Script
1.1 What Is the Tomato Script?
The Tomato Script (Tomato Jianpu Script) is a text-based notation system designed to describe numbered musical notation (Jianpu) using plain text. It draws inspiration from the ACB notation system [note: this might be the abcnotation.com] used abroad while preserving the characteristics of Chinese Jianpu.

In short, Tomato Script allows you to encode a complete Jianpu score using only text. This makes it fast to input, easy to edit, and convenient for software to process.

1.2 Structure of a Tomato Script
A complete script contains two major parts:

Header Section — Basic information such as title, composer, key, time signature, tempo, etc.
Main Body — The musical content: melody lines and lyrics.
1.3 Advantages
Fast input — Once familiar, you can type Jianpu as quickly as regular text.
Easy editing — Any text editor (Notepad, Word, mobile editors) can be used.
High-quality output — With supporting software, you can generate clean Jianpu images or MIDI audio for sharing.
4. Main Body of the Score
4.1 Structure
Each line begins with:

Q: — Melody line
C: — Lyrics line
Lyrics lines attach to the melody line immediately above them. One melody line may have multiple lyric lines.

5. Basic Notes and Rests
5.1 Notes
Numbers 1–7 represent the seven scale degrees.
A dash - extends duration.
5.2 Rests
0 — Visible rest
8 — Invisible rest (occupies space but not shown)
5.3 Percussive Notes
9 — Rhythmic/percussive note (X-style)
5.4 Octave Marks
' — Higher octave
, — Lower octave
Multiple marks may be used.
6. Duration Modifiers
6.1 Lengthening
A dash - after a note extends its duration.

6.2 Shortening
A slash / after a note shortens its duration; multiple slashes allowed.

7. Custom Beat Grouping
Because early versions grouped beats only by quarter notes, two symbols were added:

~ — Connects notes into a single beat.
^ — Forces a beat break between notes.
8. Dotted Notes
. — Dotted note
.. — Double-dotted note
9. Dynamics and Crescendo/Decrescendo
9.1 Dynamics
Add & plus the abbreviation after a note, e.g.:

&mp
&f
&pp

9.2 Crescendo / Decrescendo
< — Start crescendo
> — Start decrescendo
! — End of hairpin
If overlapping with slurs, add + to raise the hairpin.

10. Accidentals
# — Sharp
$ — Flat
= — Natural
Placed after the note number.

11. Grace Notes (Ornaments)
11.1 Front Grace Notes
Written inside [] after the main note.
Can include octave marks, slashes, and accidentals.
11.2 Back Grace Notes
Same as above, but start with [h.
Grace notes default to eighth-note length; adding / makes them sixteenth notes.
12. Accompaniment Brackets
Left bracket: &zkh
Right bracket: &ykh
Placed after the note.
13. Other Common Symbols
Many decorative symbols use & + pinyin initial. (Full table omitted here but follows the same rule.)

14. Note Annotations
Add "text" after a note to display annotation above it.

15. Barlines
15.1 Types
Various barline types are supported (single, double, final, etc.).

15.2 Hidden Barlines
|/ — Hidden, no space taken; used at line beginnings.
|* — Hidden but occupies space; used when switching to multi-voice.
16. Repeat Signs
Repeat symbols may only be placed on barlines.

17. Slurs
17.1 Basic Slurs
Use parentheses () around notes.
Slurs may nest and cross bars or lines.
17.2 Cross-line Slurs
Place the closing parenthesis on the next line.

17.3 Split Slurs
Used around page breaks or special symbols.

18. Tuplets
Tuplets use parentheses like slurs but add y after (:

(y... )

The software calculates the number of notes automatically.

19. "Hopscotch" (Jump Brackets)
Use [ for start and ] for end.
Must be placed on barlines.
Supports cross-line usage.
Add / after [ for open-ended jumps.
Add + to raise the bracket if overlapping with slurs.
If a jump begins at the start of a line, use hidden barline |/.
20. Temporary Time Signatures
Written as a barline annotation:

"p:x/x"

21. Temporary Accompaniment & Temporary Multi-Voice
21.1 Temporary Accompaniment
Use {bz... }
Notes align automatically with the main melody.
21.2 Temporary Multi-Voice
Use {dsb... }
22. Multi-Voice Notation
22.1 Voice Labels
Add a number after Q or C:

Q1:
C2:

You may add a voice name in quotes after the number.

22.2 Mixed Single and Multi-Voice
Allowed.

22.3 Custom Voice Bracket Position
Use &sbf to set bracket position manually.
Use 8 (invisible note) and |* (hidden barline) to fill empty space in other voices.
23. Pagination
Insert [fenye] on a new line to force a page break.

Note: Slurs cannot cross pages automatically; use split slurs.

24. Lyrics
24.1 Chinese Lyrics
Begin with C:
Each character corresponds to one note.
Punctuation is auto-handled.
@ skips a note.
- (duration line) does not require @.
Two characters on one note: connect with ~.
Multiple lyric lines may follow one melody line.
24.2 Lyric Annotations
Use "text" before the lyric line.
Spaces inside annotations must be written as _.
24.3 English Lyrics
Use / to separate words.
When mixing with Chinese or @, the slash may be omitted, but adding it improves readability.