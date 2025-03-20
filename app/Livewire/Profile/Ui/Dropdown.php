<?php

namespace App\Livewire\Profile\Ui;

use Livewire\Component;

class Dropdown extends Component
{

    public $isOpen = false;
    public $project;

    public function toggleDropdown()
    {
        $this->isOpen = !$this->isOpen;
    }

    public function deleteProject()
    {
        if ($this->project) {
            $this->project->delete();
            $this->dispatch('projectDelete');
        }
    }

    public function render()
    {
        return view('livewire.profile.ui.dropdown');
    }
}
