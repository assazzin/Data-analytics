#!/usr/bin/perl

@stocks=("ADVANC",
"AOT",
"BANPU",
"BBL",
"BCP",
"BDMS",
"BEAUTY",
"BEM",
"BH",
"BJC",
"BPP",
"BTS",
"CBG",
"CENTEL",
"CPALL",
"CPF",
"CPN",
"DTAC",
"EA",
"EGCO",
"GLOBAL",
"GPSC",
"HMPRO",
"INTUCH",
"IRPC",
"IVL",
"KBANK",
"KCE",
"KKP",
"KTB",
"LH",
"MINT",
"MTC",
"PSH",
"PTT",
"PTTEP",
"PTTGC",
"ROBINS",
"SAWAD",
"SCB",
"SCC",
"SPRC",
"TCAP",
"TISCO",
"TMB",
"TOP",
"TPIPP",
"TRUE",
"TU",
"WHA");

print "Stock name : ";
chomp($stock=<STDIN>);
exit if($stock eq "");
$stock = uc $stock;
foreach(@stocks) {
	if($_=~/^$stock$/) {
		goto VALID;
	}
}
print "Stock not found\n";
exit;

VALID:
print "\n";

open FILE, "StocksData/$stock.csv";
chomp(@file=<FILE>);
close FILE;
($tmp,$tmp,$tmp,$tmp,$close)=split /,/, $file[$#file];

$k4gaussian = `python k-fold-gaussian.py $stock`;
$k4linear = `python k-fold-linear.py $stock`;
$k4polynomial = `python k-fold-polynomial.py $stock`;
$predict_gaussian = `python predict-gaussian.py $stock`;
$predict_linear = `python predict-linear.py $stock`;
$predict_polynomial = `python predict-polynomial.py $stock`;
#$linear = `python linear.py $stock`;

print "Close price : $close\n\n";
print "Predict open price compare to last close price : ", $predict_gaussian;
print $k4gaussian;
print "\n";
print "Predict next open price with Linear-regression : ", $predict_linear;
print $k4linear;
print "\n";
print "Predict next open price with Polynomial-regression : ", $predict_polynomial;
print $k4polynomial;
print "\n";
#print $linear;
