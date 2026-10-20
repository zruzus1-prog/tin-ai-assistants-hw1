"""Human-review gate. Technical PASS never impersonates student authorship."""
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def validate(record):
    errors=[]
    if record.get('authorship')!='student_entered_via_review_page':errors.append('No student-entered review declaration')
    comments=record.get('comments',[])
    if len(comments)!=5 or any(len(c.get('text','').strip())<20 for c in comments):
        errors.append('Five own observations are required')
    if len(set(record.get('publisher_checks',[])))<3:errors.append('Confirm three publisher checks after opening the pages')
    if len(set(record.get('thesis_checks',[])))<3:errors.append('Confirm three thesis checks against the PDF')
    if record.get('accept_tasks') is not True:errors.append('Student acceptance of the reviewed work is pending')
    return errors
def main():
    p=ROOT/'student_review.json'
    if not p.exists():
        print('PENDING: student review has not been recorded. Open REVIEW.html.');return 2
    try:errors=validate(json.loads(p.read_text(encoding='utf-8-sig')))
    except (ValueError,TypeError):errors=['Invalid student review JSON']
    for e in errors:print('PENDING:',e)
    if errors:return 2
    print('PASS: own comments and explicit student review are recorded. Public repo URL and form submission remain separate actions.')
    return 0
if __name__=='__main__':raise SystemExit(main())
