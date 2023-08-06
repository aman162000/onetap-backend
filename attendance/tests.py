from django.test import TestCase
from attendance.models import Attendance, Student, Subject
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model
# Create your tests here.

User = get_user_model()


class AttendanceModelTest(TestCase):

    def setUp(self) -> None:
        # Create test data: students, subjects, and attendance records for testing.
        self.user = User.objects.create(
            email="alice@xyz.com", is_student=True, password="testpassword")

        self.user2 = User.objects.create(
            email="bob@abc.com", is_student=True, password="testpassword2"
        )

        self.subject = Subject.objects.create(name="Math")
        self.subject2 = Subject.objects.create(name="Science")

        # Create students and enroll them in subjects
        self.student = Student.objects.create(
            user=self.user,
            prn_no=1234567890,
            first_name="Alice",
            last_name="Bar",
            year=1
        )
        self.student2 = Student.objects.create(
            user=self.user2,
            prn_no=3456789012,
            first_name="Bob",
            last_name="Foo",
            year=1
        )
        # Enroll students in subjects
        self.student.enrolled_subjects.add(self.subject)
        self.student2.enrolled_subjects.add(self.subject)
        # Create attendance record
        self.attendance = Attendance.mark_attendance(
            self.student, self.subject, is_present=True)

    def test_create_attendance(self):
        # Test creating attendance records using create_attendance method.
        new_attendance = Attendance.mark_attendance(
            student=self.student2, subject=self.subject, is_present=True)
        self.assertTrue(new_attendance.uid)

    def test_update_attendance_status(self):
        # Test updating attendance status for a specific attendance record.
        self.attendance.update_attendance(is_present=False)
        updated_attendance = Attendance.objects.get(uid=self.attendance.uid)
        self.assertFalse(updated_attendance.is_present)

    def test_get_attendance_records_for_student(self):
        # Test retrieving attendance records for a specific student.
        student_attendance = Attendance.get_attendance_records_for_student(
            student=self.student)
        self.assertEqual(student_attendance.count(), 1)

    def test_get_attendance_records_for_subject(self):
        # Test retrieving attendance records for a specific subject.
        subject_attendance = Attendance.get_attendance_records_for_subject(
            subject=self.subject)
        self.assertEqual(subject_attendance.count(), 1)

    def test_calculate_attendance_statistics(self):
        # Test calculating attendance statistics for a specific student and subject.
        stats_student_subject = Attendance.calculate_attendance_statistics(
            student=self.student, subject=self.subject)
        self.assertEqual(stats_student_subject['total_classes'], 1)
        self.assertEqual(stats_student_subject['classes_attended'], 1)
        self.assertEqual(stats_student_subject['classes_missed'], 0)
        self.assertEqual(
            stats_student_subject['attendance_percentage'], 100.0)

    def test_delete_attendance_record(self):
        # Test deleting an attendance record.
        attendance_count_before_delete = Attendance.objects.count()
        self.attendance.delete()
        attendance_count_after_delete = Attendance.objects.count()
        self.assertEqual(attendance_count_after_delete,
                         attendance_count_before_delete - 1)

    def test_unique_constraint(self):
        # Test unique constraint on student and subject fields.
        with self.assertRaises(IntegrityError):
            Attendance.mark_attendance(
                student=self.student, subject=self.subject)

    def test_attendance_percentage_when_no_classes(self):
        # Test attendance percentage when there are no attended classes.

        # Calculate attendance statistics
        result = Attendance.calculate_attendance_statistics(
            student=self.student, subject=self.subject2)

        # Assert the attendance statistics for the student are as expected
        self.assertEqual(result['total_classes'], 0)
        self.assertEqual(result['classes_attended'], 0)
        self.assertEqual(result['classes_missed'], 0)
        self.assertEqual(result['attendance_percentage'], 0)
