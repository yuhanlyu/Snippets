denom = [["ONE HUNDRED", 10000], ["FIFTY", 5000], ["TWENTY", 2000],
         ["TEN", 1000], ["FIVE", 500], ["TWO", 200], ["ONE", 100 ],
         ["HALF DOLLAR", 50 ], ["QUARTER", 25], ["DIME", 10], ["NICKEL", 5], 
         ["PENNY", 1]]

File.open(ARGV[0]).each_line do |line|
    p, c = line.split(";").map {|s|
        d, c = s.split(".")
        d.to_i * 100 + (c || "0").to_i
    }
    c -= p
    if c < 0
        puts "ERROR"
    elsif c == 0
        puts "ZERO"
    else
        puts denom.each_with_object([]) {|(s, v), r|
            while v <= c
                r << s
                c -= v
            end
        }.join(",")
    end
end
