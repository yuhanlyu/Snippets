File.open(ARGV[0]).each_line do |line|
    a, b = line.chomp.split(";").map {|uri|
        uri.match(/^([^:]+):\/\/([^:\/]+)(:(\d+)?)?(\/.*)?$/x) {|_|
      [$1.downcase, $2.downcase, ($4 || "80"), ($5 || "/").gsub(/%(\h\h)/) {|n|
                n[1..-1].to_i(16).chr
            }]
        }
    }
    puts a == b ? "True" : "False"
end
