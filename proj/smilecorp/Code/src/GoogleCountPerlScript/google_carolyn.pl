#!C:/Perl/bin/perl


use LWP::UserAgent;
use locale;

$ua = LWP::UserAgent->new;
$ua->agent("User-Agent', 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; en) AppleWebKit/528.5+ (KHTML, like Gecko) Version/4.0 Safari/528.1");


sub makeQuery {
	my $original = shift(@_);
	$original =~s/\s+/%20/g;
	$original =~s/\"/%22/g;
	#print $original;
	return $original;
}



$in_filename = $ARGV[0];
$out_filename = $ARGV[1];
open(QUERIES, $in_filename);
open(LOGFILE, '>>' . $out_filename); #das macht append - ersetze '>>' durch '>', um es ueberschreiben zu lassen.

while($searchstring = <QUERIES>) {
# infinitive (= lemma here)
chomp $searchstring;
$search = makeQuery($searchstring);
#C print "Searching $searchstring...";

$req = HTTP::Request->new(GET => 'http://www.google.com/search?safe=off&q=' . $search .'&btnG=search&tbs=li:1' );
$res = $ua->request($req); 


	if ($res->is_success) {
	 # I've  already forgotten why I stored it to a file
	 # instead of accessing it directly?
	 # the other way could be worth a try.
	 open(QUOUT, ('>query.html'));
	 print QUOUT $res->content();
	 close(QUOUT);

	 # reading the result page
	 open(QUIN, 'query.html');
  
	       # looking for the String containing the number of results
		while($line = <QUIN>) {

	   		# for the English result page this matches - 
	   		# if there are any results, that is.
	   		if ($line =~ /About.(([0-9]++,)*([0-9]++)).+results/) { 
	   			$rechits = $1; #no of hits, as string
	   			# visual control...
                                #C print "Results: $1 ($2 $3) \n"; #there used to be an ugly bug here, the visual control helps checking for it.
			} 
		}
		close(QUIN);
	 	# get rid of the points / commas within the number of hits.      
	 	$rechits =~ s/\D//g;
                #print "$rechits\n";
	 	print LOGFILE "$rechits\t$searchstring\n";
 
	
	} else {
		print "Query not successfull";
	}
}
close(QUERIES);
close(LOGFILE);


