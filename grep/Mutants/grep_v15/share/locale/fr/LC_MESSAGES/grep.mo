��    4      �  G   \      x  
  y  0  �  t  �  $   *    O  v  c     �     �       ,         M  %   k  ,   �  -   �      �  &        4     T     t     v     �  E   �     �     �  �   
  (   �     �  �   �  &   n     �     �     �     �     �  )   �  (        8     :     Y     u     �     �     �     �     �     �          (     ?     Z     k  <  z  E  �  X  �  &  V  2   }&  1  �&  �  �'     �)  !   �)  !   *  2   -*  !   `*  +   �*  2   �*  3   �*  $   +  +   :+  *   f+  *   �+     �+     �+     �+  E   �+     3,     D,  �   \,  /   -      2-  �   S-  1   .     ?.     K.     W.  &   c.     �.  +   �.  *   �.     �.  .   �.  4   */  *   _/     �/  !   �/     �/     �/  "   �/  #   0     00  &   P0      w0     �0     �0     $                    /      ,      0      "               -   )   *   3          4                                                  &             2          '   %          !                1                     
       .   (   +   	   #                 
Context control:
  -B, --before-context=NUM  print NUM lines of leading context
  -A, --after-context=NUM   print NUM lines of trailing context
  -C, --context=NUM         print NUM lines of output context
  -NUM                      same as --context=NUM
      --color[=WHEN],
      --colour[=WHEN]       use markers to distinguish the matching string
                            WHEN may be `always', `never' or `auto'.
  -U, --binary              do not strip CR characters at EOL (MSDOS)
  -u, --unix-byte-offsets   report offsets as if CRs were not there (MSDOS)

`egrep' means `grep -E'.  `fgrep' means `grep -F'.
With no FILE, or when FILE is -, read standard input.  If less than
two FILEs given, assume -h.  Exit status is 0 if match, 1 if no match,
and 2 if trouble.
 
Miscellaneous:
  -s, --no-messages         suppress error messages
  -v, --invert-match        select non-matching lines
  -V, --version             print version information and exit
      --help                display this help and exit
      --mmap                use memory-mapped input if possible
 
Output control:
  -m, --max-count=NUM       stop after NUM matches
  -b, --byte-offset         print the byte offset with output lines
  -n, --line-number         print line number with output lines
      --line-buffered       flush output on every line
  -H, --with-filename       print the filename for each match
  -h, --no-filename         suppress the prefixing filename on output
      --label=LABEL         print LABEL as filename for standard input
  -o, --only-matching       show only the part of a line matching PATTERN
  -q, --quiet, --silent     suppress all normal output
      --binary-files=TYPE   assume that binary files are TYPE
                            TYPE is 'binary', 'text', or 'without-match'
  -a, --text                equivalent to --binary-files=text
  -I                        equivalent to --binary-files=without-match
  -d, --directories=ACTION  how to handle directories
                            ACTION is 'read', 'recurse', or 'skip'
  -D, --devices=ACTION      how to handle devices, FIFOs and sockets
                            ACTION is 'read' or 'skip'
  -R, -r, --recursive       equivalent to --directories=recurse
      --include=PATTERN     files that match PATTERN will be examined
      --exclude=PATTERN     files that match PATTERN will be skipped.
      --exclude-from=FILE   files that match PATTERN in FILE will be skipped.
  -L, --files-without-match only print FILE names containing no match
  -l, --files-with-matches  only print FILE names containing matches
  -c, --count               only print a count of matching lines per FILE
  -Z, --null                print 0 byte after FILE name
 
Report bugs to <bug-grep@gnu.org>.
   -E, --extended-regexp     PATTERN is an extended regular expression
  -F, --fixed-strings       PATTERN is a set of newline-separated strings
  -G, --basic-regexp        PATTERN is a basic regular expression
  -P, --perl-regexp         PATTERN is a Perl regular expression
   -e, --regexp=PATTERN      use PATTERN as a regular expression
  -f, --file=FILE           obtain PATTERN from FILE
  -i, --ignore-case         ignore case distinctions
  -w, --word-regexp         force PATTERN to match only whole words
  -x, --line-regexp         force PATTERN to match only whole lines
  -z, --null-data           a data line ends in 0 byte, not newline
 %s (GNU grep) %s
 %s: illegal option -- %c
 %s: invalid option -- %c
 %s: option `%c%s' doesn't allow an argument
 %s: option `%s' is ambiguous
 %s: option `%s' requires an argument
 %s: option `--%s' doesn't allow an argument
 %s: option `-W %s' doesn't allow an argument
 %s: option `-W %s' is ambiguous
 %s: option requires an argument -- %c
 %s: unrecognized option `%c%s'
 %s: unrecognized option `--%s'
 ' (standard input) Binary file %s matches
 Copyright 1988, 1992-1999, 2000, 2001 Free Software Foundation, Inc.
 Memory exhausted No syntax specified Search for PATTERN in each FILE or standard input.
Example: %s -i 'hello world' menu.h main.c

Regexp selection and interpretation:
 The -P and -z options cannot be combined The -P option is not supported This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 Try `%s --help' for more information.
 Unbalanced ( Unbalanced ) Unbalanced [ Unfinished \ escape Unknown system error Usage: %s [OPTION]... PATTERN [FILE] ...
 Usage: %s [OPTION]... PATTERN [FILE]...
 ` conflicting matchers specified input is too large to count invalid context length argument invalid max count malformed repeat count memory exhausted out of memory recursive directory loop unfinished repeat count unknown binary-files type unknown devices method unknown directories method warning: %s: %s
 writing output Project-Id-Version: GNU grep 2.5g
POT-Creation-Date: 2002-01-22 14:39+0100
PO-Revision-Date: 2002-03-17 20:00-0500
Last-Translator: Michel Robitaille <robitail@IRO.UMontreal.CA>
Language-Team: French <traduc@traduc.org>
MIME-Version: 1.0
Content-Type: text/plain; charset=ISO-8859-1
Content-Transfer-Encoding: 8-bit
 
Contr�le du contexte:
  -B, --before-context=N    imprimer N lignes du contexte d'en-t�te
  -A, --after-context=N     imprimer N lignes du contexte finale
  -C, --context[=N]         imprimer N lignes (2 par d�faut) du contexte
                            � moins que -A ou -B ne soit sp�cifi�
  -N                        identique � --context=N
      --color[=DATE],
      --colour[=DATE]       utiliser des marqueurs pour distinguer les
                            cha�nes concordantes
  -U, --binary              ne pas enlever les caract�res CR sur 
                            les fins de lignes (MS-DOS)
  -u, --unix-byte-offsets   afficher les adresses relatives comme si
                            aucun CR n'�tait pr�sent (MS-DOS)

� egrep � est �quivalent � � grep -E �. � fgrep � est �quivalent � � grep -F �.
Sans FICHIER, ou si - est utilis� comme nom de FICHIER, la lecture
se fait de l'entr�e standard. S'il y a moins de 2 FICHIERS, l'option -h
est implicite. Termine avec 0 s'il y a concordance avec 1 si aucune.
Termine avec 2 s'il y a des erreurs de syntaxe ou de syst�me.
 
Divers:
  -s, --no-messages         supprimer les messages d'erreur
  -v, --revert-match        s�lectionner les lignes sans concordances
  -V, --version             afficher le nom et la version du logiciel
      --help                afficher l'aide et quitter
      --mmap                utiliser la table de m�moire � l'entr�e si possible
 
Contr�le de sortie:
  -m, --max-count=N         arr�ter apr�s N concordances
  -b, --byte-offset         afficher les adresses relatives des
                            lignes trait�es
  -n, --line-number         afficher les num�ros de lignes des
                            lignes trait�es
      --line-buffered       vider la sortie pour chaque ligne
  -H, --with-filename       afficher le nom de fichier pour
                            chaque concordance
  -h, --no-filename         supprimer le pr�fixe du nom de fichier
                            sur la sortie
      --label=ETIQUETTE     afficher l'�TIQUETTE comme un nom de
                            fichier sur l'entr�e standard
  -o, --only-matching       afficher la partie d'une ligne concordant avec le PATRON
  -q, --quiet, --silent     supprimer tout affichage en sortie
      --binary-files=TYPE   assumer que les fichiers binaires sont de
                            TYPE soit � binary �, � text �, ou � without-match �,
  -a, --text                ne pas supprimer la sortie binaire
  -I                        �quivalent � --binary-files=without-match
  -d, --directories=ACTION  traiter les r�pertoires selon l'ACTION
                            � read � (lecture), � recurse � (r�cursivit�),
                            ou � skip � (escamotage).
  -R, -r, --recursive       �quivalent � --directories=recurse
      --include=PATRON      fichiers concordant au PATRON seront examin�s
      --exclude=PATRON      fichiers concordant au PATRON ne seront pas examin�s
      --exclude-from=FICHIER  fichiers dont le PATRON concorde dans le fichierseront escamot�s
  -L, --files-without-match afficher seulement les noms des fichiers
                            ne contenant pas de concordance
  -l, --files-with-matches  afficher seulement les noms des fichiers
                            contenant des concordances
  -c, --count               afficher seulement le d�compte des lignes
                            concordantes par fichier
  -Z, --null                afficher l'octet Z�RO apr�s le nom du fichier
 
Rapporter toutes anomalies � <bug-grep@gnu.org>.
   -E, --extended-regexp     PATRON est une expression reguli�re �tendue
  -F, --fixed-regexp        PATRON est une cha�ne fixe s�par�e par des retour de chariot
  -G, --basic-regexp        PATRON est une expression r�guli�re de base
  -P, --perl-regexp         PATRON est une expression r�guli�re en Perl
   -e, --regexp=PATTERN      utiliser le PATRON comme expression r�guli�re
  -f, --file=FILE           obtenir le PATRON du FICHIER
  -i, --ignore-case         ignorer la distrinction de la casse
  -w, --word-regexp         forcer l'appariement du PATRON que sur des mots complets
  -x, --line-regexp         forcer l'appariement du PATRON que sur des lignes enti�res
  -z, --null-data           terminer la ligne de donn�es par Z�RO et
                            non pas par un retour de chariot
 %s (grep de GNU) %s
 %s: l'option -- %c est ill�gale.
 %s: l'option -- %c est invalide.
 %s: l'option � %c%s � ne permet pas de param�tre.
 %s: l'option � %s � est ambigu�.
 %s: l'option � %s � requiert un param�tre.
 %s: l'option � --%s � ne permet pas de param�tre.
 %s: l'option � -W %s � ne permet pas de param�tre.
 %s: l'option � -W %s � est ambigu�.
 %s: l'option  -- %c requiert un param�tre.
 %s: l'option � %c%s � n'est pas reconnue.
 %s: l'option � --%s � n'est pas reconnue.
 ' (entr�e standard) Fichier binaire %s concorde
 Copyright 1988, 1992-1999, 2000, 2001 Free Software Foundation, Inc.
 M�moire �puis�e. Aucune syntaxe sp�cifi� Recherche du PATRON dans chaque FICHIER ou sur l'entr�e standard.
Exemple: %s -i 'hello world� menu.h main.c

S�lection et interpr�tation de l'expression r�guli�re:
 Les options -P et -z ne peuvent �tre combin�es. L'option -P n'est pas support�e. Ce logiciel est libre; voir les sources pour les conditions de
reproduction. AUCUNE garantie n'est donn�e; tant pour des raisons
COMMERCIALES que pour R�PONDRE � UN BESOIN PARTICULIER.
 Pour en savoir davantage, faites: � %s --help �.
 ( non pair� ) non pair� [ non pair� s�quence d'�chappement \ non termin�e. Erreur syst�me inconnue Usage: %s [OPTION]... PATRON [FICHIER] ...
 Usage: %s [OPTION]... PATRON [FICHIER]...
 ` op�rateurs de concordance sp�cifi�s en conflit ce qui est en entr�e est trop grand pour �tre compt� param�tre de contexte de longueur invalide d�compte maximal invalide. d�compte de r�p�tition mal form�. M�moire �puis�e. M�moire �puis�e. boucle r�cursive sur le r�pertoire d�compte de r�p�tition non termin�. type de fichier binaire inconnu m�thode inconnue pour les p�riph�rique m�thode inconnue des r�pertoires AVERTISSEMENT: %s: %s
 G�n�ration du r�sultat. 