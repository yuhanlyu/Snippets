File.open(ARGV[0]).each_line do |line|
    puts line.gsub(/\D/, "")
             .each_char
             .map(&:to_i)
             .each_with_index
             .inject(0) { |sum, (n, i)| 
              sum += n * (i % 2 == 0 ? 2 : 1) } % 10 == 0 ? "Real" : "Fake"
end
