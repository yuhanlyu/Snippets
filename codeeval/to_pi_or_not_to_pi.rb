require "bigdecimal"
require "bigdecimal/math"
d = BigMath::PI(5001).to_s[2..-1]
File.open(ARGV[0]).each_line do |line|
    puts d[line.to_i - 1]
end
