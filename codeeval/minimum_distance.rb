File.open(ARGV[0]).each_line do |line|
    adds = line.split.slice(1..-1).map(&:to_i).sort
    mid = adds.length / 2;
    ans = adds.length.even? ? (adds[mid] + adds[mid - 1]) / 2 : adds[mid]
    puts adds.inject(0) {|s, x| s += (x - ans).abs}
end
