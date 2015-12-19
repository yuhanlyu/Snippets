File.open(ARGV[0]).each_line do |line|
    wines, letters = line.chomp.split(' | ')
    wines, result = wines.split, []
    count = Hash.new(0)
    letters.each_char {|c| count[c] += 1}
    wines.each do |wine|
        word_count = Hash.new(0)
        wine.each_char {|c| word_count[c] += 1}
        result.push(wine) if count.all? {|c, m| word_count[c] >= m}
    end
    puts result.length > 0 ? result.join(' ') : "False"
end
