File.open(ARGV[0]).each_line do |line|
    result = [[0, 1, 0]]
    1.upto(line.to_i - 1) do
        result << [0] + result[-1].each_cons(2).map {|a, b| a + b} + [0]
    end
    puts result.map {|l| l[1...-1]}.flatten.map(&:to_s).join(" ")
end
