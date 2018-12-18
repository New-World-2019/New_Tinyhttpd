<<<<<<< HEAD
#!/usr/local/bin/perl -Tw
=======
#!/usr/bin/perl -Tw
>>>>>>> 1d0ddd61a7c75c809c58cca3fda0cd3972235bd4

use strict;
use CGI;

my($cgi) = new CGI;

print $cgi->header;
my($color) = "blue";
$color = $cgi->param('color') if defined $cgi->param('color');

print $cgi->start_html(-title => uc($color),
                       -BGCOLOR => $color);
print $cgi->h1("This is $color");
print $cgi->end_html;
<<<<<<< HEAD
=======

>>>>>>> 1d0ddd61a7c75c809c58cca3fda0cd3972235bd4
