require 'json'
File.open(ARGV[0]).each_line do |line|
    puts JSON.parse(line)['menu']['items'].compact
             .select { |item| item['label'] }
             .inject(0) { |acc, item| acc + item['id'].to_i }
end
