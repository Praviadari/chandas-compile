from core.benchmark import BenchmarkEntry, evaluate_entry
from core.meter_validator import analyze_text

entry = BenchmarkEntry(
    name='test',
    text='PALLAVI: రామ ప్రేమ\nCHARANAM: రామ సుఖం\n',
    expected_patterns={'PALLAVI': [[1, 0, 1, 0]], 'CHARANAM': [[1, 0, 1, 0]]},
)
print('pallavi units', analyze_text('రామ ప్రేమ'))
print('charanam units', analyze_text('రామ సుఖం'))
print('report', evaluate_entry(entry))
