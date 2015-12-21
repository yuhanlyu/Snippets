File.open(ARGV[0]).each_line do |line|
    counts = line.split
                 .map(&:to_i)
                 .each_with_object(Array.new(10) {Array.new})
                 .with_index { |(num, idx), i| idx[num].push(i + 1) }
    puts (low = (1..9).find {|i| counts[i].length == 1}) ? counts[low][0] : 0
end
